from django.urls import path


from .views import OrderUpdateView, OrderListView, OrderCreateView, OrderDetailView,  \
    EmployeeStatisticsView

urlpatterns = [
    path('order/', OrderCreateView.as_view(), name='order-list'),
    path('order-create/', OrderListView.as_view(), name='order-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order-update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),

    path('employee-statistic/<int:id>/', EmployeeStatisticsView.as_view(), name='employee_statistic'),
    # path('allemployee-statistic/', AllEmployeeStatisticsView.as_view(), name='employee-statistic'),

]