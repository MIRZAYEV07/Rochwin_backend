from django.urls import path


from .views import ClientCreateView,ClientDetailView,ClientUpdateView,ClientListView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients-create/', ClientCreateView.as_view(), name='client-create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='product-detail'),
    path('client-update/<int:pk>/', ClientUpdateView.as_view(), name='product-update'),


]