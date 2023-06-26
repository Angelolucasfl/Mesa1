from django.contrib import admin
from .models import Employee, Contractor, ContractorRating, EmployeeRating, Service

class ContractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_average_rating']  # Define quais campos exibir na lista
    readonly_fields = ['get_average_rating']  # Define quais campos são somente leitura

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    get_average_rating.short_description = 'Nota média'  # Define o nome da coluna na lista


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_average_rating')
    readonly_fields = ['get_average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    get_average_rating.short_description = 'Nota média'


class ContractorRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'contractor', 'rating']

class EmployeeRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'rating']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_calc_value']

    def display_calc_value(self, obj):
        return obj.calc_value()

    display_calc_value.short_description = 'Valor do serviço'

admin.site.register(Service, ServiceAdmin)
admin.site.register(ContractorRating, ContractorRatingAdmin)
admin.site.register(EmployeeRating, EmployeeRatingAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Employee, EmployeeAdmin)

