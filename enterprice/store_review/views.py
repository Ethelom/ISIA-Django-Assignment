from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from store_review.models import Purchase, LineItem, Customer, Store, StoreReview
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='login')
def view_purchases(request):
    username = request.user.username
    purchases = Purchase.objects.filter(customer_id=username).order_by('-purchase_date')
    reviewed_purchase_ids = list(StoreReview.objects.values_list('purchase_id', flat=True).filter(customer_id=username))
    purchases_that_have_been_reviewed = []
    for purchase in purchases:
        if purchase.purchase_id in reviewed_purchase_ids:
            purchases_that_have_been_reviewed.append(purchase)
    context = {
        "purchases": purchases,
        "purchases_that_have_been_reviewed": purchases_that_have_been_reviewed
    }
    return render(request, 'store_review/my_purchases.html', context)


@login_required(login_url='login')
def write_review(request, purchase_id):
    try:
        store_review = StoreReview.objects.get(purchase_id=purchase_id)
    except StoreReview.DoesNotExist:
        store_review = None
    if store_review is not None:
        # edit review
        context = {
            "store_review": store_review,
            "purchase": store_review.purchase,
            "stars": [1, 2, 3, 4, 5],
        }
    else:
        # write new review
        purchase = Purchase.objects.get(purchase_id=purchase_id)
        context = {
            "purchase": purchase,
            "stars": [1, 2, 3, 4, 5],
        }
    return render(request, 'store_review/write_review.html', context=context)


@login_required(login_url='login')
def delete_review(request, purchase_id):
    store_review = StoreReview.objects.get(purchase_id=purchase_id)
    store_username = store_review.store.username
    store_review.delete()
    return HttpResponseRedirect(reverse('view-store-profile', args=(store_username,)))


@login_required(login_url='login')
def submit_review(request):
    rating = request.POST['rating']
    review_body = request.POST['review-body']
    purchase_id = request.POST['purchase-id']
    purchase = Purchase.objects.get(purchase_id=purchase_id)
    customer = Customer.objects.get(username=request.user.username)
    store_review = StoreReview(rating=rating, review_body=review_body, customer=customer, store=purchase.store,
                               purchase=purchase)
    store_review.save()
    return HttpResponseRedirect(reverse('view-store-profile', args=(purchase.store.username,)))


@login_required(login_url='login')
def view_store_profile(request, store_username):
    store = Store.objects.get(username=store_username)
    store_reviews = StoreReview.objects.filter(store=store)
    avg_rating = 0
    total_reviews = len(store_reviews)
    if total_reviews > 0:
        for review in store_reviews:
            avg_rating += review.rating
        avg_rating = avg_rating / len(store_reviews)
    context = {
        "average_rating": avg_rating,
        "store": store,
        "store_reviews": store_reviews,
        "stars": [1, 2, 3, 4, 5],
        "username": request.user.username,
    }
    return render(request, 'store_review/store_profile.html', context=context)
