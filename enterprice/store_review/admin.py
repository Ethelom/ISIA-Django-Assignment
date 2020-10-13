from django.contrib import admin
from .models import Customer, Store, StoreReview, Product, Purchase, LineItem

admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(LineItem)
admin.site.register(Purchase)
admin.site.register(StoreReview)
