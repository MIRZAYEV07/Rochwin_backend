from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductUpdateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products-update/<int:pk>/', ProductUpdateView.as_view(), name='product-detail'),

]

