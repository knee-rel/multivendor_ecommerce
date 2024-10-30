# inventory/models.py
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.product} ordered quantity {self.order_quantity}"

class ShippingTracking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PND', 'Pending'
        SHIPPED = 'SHP', 'Shipped'
        IN_TRANSIT = 'ITR', 'In Transit'
        DELIVERED = 'DLV', 'Delivered'
        RETURNED = 'RTN', 'Returned'
        CANCELLED = 'CNL', 'Cancelled'
        
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.PENDING)
    shipped_date = models.DateTimeField(null=True)
    delivery_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"Tracking {self.tracking_number} for Order {self.order.id}"