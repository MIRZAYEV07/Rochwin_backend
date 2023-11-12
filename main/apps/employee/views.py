from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer




class EmployeeCreateView(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListView(generics.ListAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'



class EmployeeUpdateView(generics.UpdateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'