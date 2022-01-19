from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

from .models import Employee
from .serializer import EmployeeSerializer

# Create your views here."
@api_view(['GET'])
def apiView(request):
    web_urls = {
     'List':'/list/',
     'Detail View':'/details/<int:pk>/',
     'Create':'/create/',
     'Update':'/update/<int:pk>/',
     'Delete':'/create//<int:pk>/',  
    }

    return Response(web_urls)

@api_view(['GET'])
def employee_list(request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True )
        return JsonResponse(serializer.data, safe= False)


@api_view(['GET'])
def employee_detail(request, pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee )
        return JsonResponse(serializer.data)



@api_view(['POST'])
def post_employee(request):
        serializer = EmployeeSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)




    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = EmployeeSerializer(data=data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status =200)
    #     return JsonResponse(serializer.errors, status = 400)



# @csrf_exempt
# def employee_detail(request, pk):
#     try:
#         single = Employee.objects.get(id=pk)
    
#     except Employee.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = EmployeeSerializer(single) 
#         return (serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = EmployeeSerializer(single, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         single.delete()
#         return HttpResponse(status=204)


    