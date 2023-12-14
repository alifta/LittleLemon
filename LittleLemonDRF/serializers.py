# Django
from decimal import Decimal
from django.contrib.auth.models import User

# REST
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

# Model
from .models import Category, MenuItem, Cart, Order, OrderItem, Rating


class UserSerilializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class MenuItemSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "category", "featured"]


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        attrs["price"] = attrs["quantity"] * attrs["unit_price"]
        return attrs

    class Meta:
        model = Cart
        fields = ["user", "menuitem", "unit_price", "quantity", "price"]
        extra_kwargs = {"price": {"read_only": True}}


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["order", "menuitem", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer(many=True, read_only=True, source="order")

    class Meta:
        model = Order
        fields = ["id", "user", "delivery_crew", "status", "date", "total", "orderitem"]


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Rating
        fields = ["user", "menuitem_id", "rating"]
        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(), fields=["user", "menuitem_id"]
            )
        ]
        extra_kwargs = {
            "rating": {"max_value": 5, "min_value": 0},
        }
