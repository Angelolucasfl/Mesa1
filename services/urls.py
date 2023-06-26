from django.urls import path
from . views import ServiceView, ServiceDetailView

urlpatterns = [
    path('services/', ServiceView),
    path('service-detail/<int:pk>/', ServiceDetailView),
]