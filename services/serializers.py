from rest_framework import serializers
from . models import Employee, Contractor, ContractorRating, EmployeeRating, Service

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'bio', 'available', 'created_at', 'updated_at']


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ['id', 'name', 'bio', 'created_at', 'updated_at']


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
        fields = ['id', 'title', 'description', 'hours', 'hours_value', 'contractor', 'enlisted', 'chosen_employee', 'created_at', 'updated_at', 'address', 'service_date', 'start_time', 'image']


