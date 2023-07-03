from django.urls import path
from . views import ServiceView, ServiceDetailView, ContractorView, ContractorDetailView, EmployeeView, EmployeeDetailView

urlpatterns = [
    path('services/', ServiceView),
    path('service-detail/<int:pk>/', ServiceDetailView),

    path('contractors/', ContractorView),
    path('contractor-detail/<int:pk>/', ContractorDetailView),

    path('employees/', EmployeeView),
    path('employee-detail/<int:pk>/', EmployeeDetailView),
]

