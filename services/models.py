from django.db import models
from decimal import Decimal

class Contractor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    email = models.EmailField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_average_rating(self):
        ratings = ContractorRating.objects.filter(contractor=self)
        total_ratings = ratings.count()
        if total_ratings > 0:
            sum_ratings = sum(rating.rating for rating in ratings)
            return sum_ratings / total_ratings
        else:
            return 0
        
    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255) 
    bio = models.TextField(null=True)
    email = models.EmailField(unique=True, blank=True)
    available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_average_rating(self):
        ratings = EmployeeRating.objects.filter(employee=self)
        total_ratings = ratings.count()
        if total_ratings > 0:
            sum_ratings = sum(rating.rating for rating in ratings)
            return sum_ratings / total_ratings
        else:
            return 0
        
    def __str__(self):
        return self.name


class ContractorRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"Contractor Rating {self.rating} from {self.contractor.name} to {self.employee.name}"


class EmployeeRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"Employee Rating {self.rating} from {self.employee.name} to {self.contractor.name}"
    

# models.py
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    hours = models.TimeField()
    hours_value = models.DecimalField(max_digits=8, decimal_places=2)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    enlisted = models.ManyToManyField(Employee, related_name='enlisted_services', blank=True)
    chosen_employee = models.ForeignKey(Employee, related_name='chosen_services', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, default='N/A')
    service_date = models.DateField()
    start_time = models.TimeField(default='00:00')
    image = models.ImageField(upload_to='media/service_images/', default='media/service_images/default.jpg')

    def calc_value(self):
        if self.hours:
            total_minutes = self.hours.hour * 60 + self.hours.minute
            valor_sem_taxa = total_minutes * self.hours_value / 60
            taxa = valor_sem_taxa * Decimal('0.1')
            valor_total = valor_sem_taxa + taxa
            return valor_total
        return 0

    def __str__(self):
        return self.title








    