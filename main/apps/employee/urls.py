from django.urls import path


from .views import EmployeeCreateView,EmployeeDetailView,EmployeeUpdateView,EmployeeListView

urlpatterns = [
    path('employee-create/', EmployeeCreateView.as_view(), name='employee-list'),
    path('employees/', EmployeeListView.as_view(), name='employee-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee-update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),



]