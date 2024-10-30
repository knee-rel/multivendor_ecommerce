# inventory/admin.py
from django.contrib import admin
from inventory.models import Product, Order, UserProfile, Category

admin.site.site_header = "Inventory Admin"

class CategoryAdmin(admin.ModelAdmin):  # Admin class for Category
    model = Category
    list_display = ("name",)
    search_fields = ("name",)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("name", "category", "quantity")
    list_filter = ["category"]
    search_fields = ["name"]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("product", "created_by", "order_quantity", "date")
    list_filter = ["date"]
    search_fields = ["product"]


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "physical_address", "mobile", "picture")
    list_filter = ["user"]
    search_fields = ["user"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
