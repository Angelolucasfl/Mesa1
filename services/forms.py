from . models import Employee, Service
from django import forms

class ServiceForm(forms.ModelForm):
    enlisted = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': 10}),
        required=False,
    )

    chosen_employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=False,
    )

    class Meta:
        model = Service
        fields = '__all__'
