from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status



class EmployeeList(APIView):

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        print("serializer.data ", serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Employee = self.get_object(pk)
        Employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)		