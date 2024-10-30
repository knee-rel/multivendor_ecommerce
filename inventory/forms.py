# inventory/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from inventory.models import Product, Order, Category, ShippingTracking


class UserRegistry(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

class CategoryForm(forms.ModelForm):  # Form for Category
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "quantity", "description"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]

class ShippingTrackingForm(forms.ModelForm):
    class Meta:
        model = ShippingTracking
        fields = ['order', 'tracking_number', 'status', 'shipped_date', 'delivery_date']
        widgets = {
            'shipped_date': forms.DateInput(attrs={'class': 'form-control', 'id': 'shipped_date'}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'id': 'delivery_date'}),
        }
