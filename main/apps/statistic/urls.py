from django.urls import path
from .views import EmployeeStatisticsView, AllEmployeeStatisticsView, ClientStatisticsView

urlpatterns = [
    path('statistics/employee/<int:id>/', EmployeeStatisticsView.as_view(), name='employee-statistics'),
    path('statistics/employees/', AllEmployeeStatisticsView.as_view(), name='all-employee-statistics'),
    path('statistics/client/<int:id>/', ClientStatisticsView.as_view(), name='client-statistics'),
]
