from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product, Category, CartItem, Order
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'categories']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'postal_code', 'delivery_method']