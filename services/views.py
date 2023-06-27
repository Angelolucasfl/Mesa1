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
    

@api_view(['GET'])
def ServiceDetailView(request, pk):

    try:
        service = Service.objects.get(id=pk)
    except service.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
        