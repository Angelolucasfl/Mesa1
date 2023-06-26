from rest_framework import serializers
from . models import Employee, Contractor, ContractorRating, EmployeeRating, Service

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'bio', 'available', 'created_at', 'updated_at']


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ['name', 'bio', 'address', 'created_at', 'updated_at']


class ContractorRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorRating
        fields = ['contractor', 'employee', 'rating']


class EmployeeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRating
        fields = ['employee', 'contractor', 'rating']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title', 'description', 'hours', 'hours_value', 'contractor', 'enlisted', 'created_at', 'updated_at']



