from django.contrib import admin
from django.urls import path
from products import views
from django.shortcuts import redirect


urlpatterns = [
    path('',views.ProductViewSet.as_view(), name = "index"),
    path('<int:pk>/', views.ProductDetailViewSet.as_view(), name="product-detail"),
    path('sellers/', views.SellerViewSet.as_view(), name="seller-list"),
    path('<int:pk>/', views.SellerDetailViewSet.as_view(), name="seller-detail"),
    path('',lambda request: redirect('products/',permanent=False))
]
