from django.urls import path
from .views import ServiceView, ServiceDetailView, ContractorView, ContractorDetailView, EmployeeView, EmployeeDetailView, EmployeeRatingView, ContractorRatingView, check_email

urlpatterns = [
    path('services/', ServiceView),
    path('service-detail/<int:pk>/', ServiceDetailView),

    path('contractors/', ContractorView),
    path('contractor-detail/<int:pk>/', ContractorDetailView),

    path('employees/', EmployeeView),
    path('employee-detail/<int:pk>/', EmployeeDetailView),

    path('check-email/', check_email),  # Rota sem parâmetro

    path('rating-employee/', EmployeeRatingView),
    path('rating-contractor/', ContractorRatingView),
]


