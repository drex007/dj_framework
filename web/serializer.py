from rest_framework import serializers
from rest_framework import Employee

class EmployeeSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length= 100)
    secondname = serializers.CharField(max_length= 100)
    employer_id = serializers.IntegerField()


    
