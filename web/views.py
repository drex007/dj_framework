from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from .serializer import EmployeeSerializer

# Create your views here.

def employee_list(request):

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True )
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = EmployeeSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status =200)
        return JsonResponse(serializer.errors, status = 400)



@csrf_exempt
def employee_detail(request, pk):
    try:
        single_employee = Employee.objects.get(pk=pk)
    
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(single_employee)
        return (serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = EmployeeSerializer(single_employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        single_employee.delete()
        return HttpResponse(status=204)


    