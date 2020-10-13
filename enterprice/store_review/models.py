from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Store(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=25)
    store_name = models.CharField(max_length=40)
    email = models.CharField(max_length=45)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=5)
    store_image = models.CharField(max_length=100)


class Customer(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=25)
    fullname = models.CharField(max_length=40)
    user_image = models.CharField(max_length=100)


class Product(models.Model):
    product_name = models.CharField(max_length=50, primary_key=True)
    product_img = models.CharField(max_length=100)
    category = models.CharField(max_length=20)


class LineItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()


class Purchase(models.Model):
    purchase_id = models.IntegerField(primary_key=True)
    purchase_date = models.DateField(default=datetime.date.today)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lineItems = models.ManyToManyField(LineItem)


class StoreReview(models.Model):
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_body = models.CharField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE, primary_key=True)
