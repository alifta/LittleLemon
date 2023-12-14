from django.urls import path
from . import views

urlpatterns = [
    # Categories
    path("categories", views.CategoriesView.as_view()),
    # TODO: Need to implement the view class "SingleCategoryView"
    # path("categories/<int:pk>", views.SingleCategoryView.as_view()),
    # Menu-items
    path("menu-items", views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    # Carts
    path("cart/menu-items", views.CartView.as_view()),
    # Orders
    path("orders", views.OrderView.as_view()),
    path("orders/<int:pk>", views.SingleOrderView.as_view()),
    # Groups
    path(
        "groups/manager/users",
        views.GroupViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
    path(
        "groups/delivery-crew/users",
        views.DeliveryCrewViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
    # Ratings
    path("ratings", views.RatingsView.as_view()),
]
