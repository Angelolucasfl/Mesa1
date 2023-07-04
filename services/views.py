from . models import Service, EmployeeRating, ContractorRating, Employee, Contractor
from . serializers import ServiceSerializer, ContractorRatingSerializer, EmployeeRatingSerializer, EmployeeSerializer, ContractorSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def ServiceView(request):

    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def ServiceDetailView(request, pk):
    try:
        service = Service.objects.get(id=pk)
    except service.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)

        if serializer.is_valid():
            enlisted_ids = request.data.get('enlisted', [])  # Obtém a lista de IDs dos funcionários alistados
            enlisted_employees = Employee.objects.filter(id__in=enlisted_ids)  # Obtém os objetos dos funcionários alistados

            serializer.save(enlisted=enlisted_employees)  # Salva o serviço e associa os funcionários alistados

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=204)
    

@api_view(['GET', 'POST'])
def ContractorView(request):

    if request.method == 'GET':
        contractors = Contractor.objects.all()
        serializer = ContractorSerializer(contractors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContractorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ContractorDetailView(request, pk):
    try:
        contractor = Contractor.objects.get(pk=pk)
    except Contractor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContractorSerializer(contractor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContractorSerializer(contractor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contractor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
@api_view(['GET', 'POST'])
def EmployeeView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def EmployeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def ContractorRatingView(request):
    if request.method == 'GET':
        ratings = ContractorRating.objects.all()
        serializer = ContractorRatingSerializer(ratings, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ContractorRatingSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def EmployeeRatingView(request):
    if request.method == 'GET':
        ratings = EmployeeRating.objects.all()
        serializer = EmployeeRatingSerializer(ratings, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmployeeRatingSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)