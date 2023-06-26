from django.db import models
import decimal


class Contractor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    address = models.CharField(max_length=255)
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


class Service(models.Model):
    title= models.CharField(max_length=255) 
    description= models.TextField()
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    hours_value = models.DecimalField(max_digits=8, decimal_places=2)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    enlisted = models.ManyToManyField(Employee, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def calc_value(self):
        valor_sem_taxa = self.hours * self.hours_value
        taxa = valor_sem_taxa * decimal.Decimal('0.1')
        valor_total = valor_sem_taxa + taxa
        return valor_total
    
    def __str__(self):
        return self.title
    