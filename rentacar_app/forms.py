from django import forms
from .models import Customer, Rent

class CarForm(forms.Form):
    input_id = None
    input_model = forms.CharField(label='Model', max_length=100)
    input_plate = forms.CharField(label='Plate', max_length=100)
    input_brand = forms.CharField(label='Brand', max_length=100)
    input_color = forms.CharField(label='Color', max_length=100)
    input_price = forms.FloatField(label='Price per day')

class CustomerForm(forms.Form):
    input_id = None
    input_name = forms.CharField(label='Name', max_length=100)
    input_cpf = forms.CharField(label='CPF', max_length=14)
    input_birthday = forms.DateField(label='Birthday', widget=forms.DateInput(format='%d/%m/%Y'),
                                     input_formats=['%d-%m-%Y','%d/%m/%Y', '%d/%m/%y'])

class RentForm(forms.Form):

    input_customer = forms.ChoiceField(label='Customer')
    input_number_of_days = forms.IntegerField(label='Number of days')

    def __init__(self, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)

        rented_customers = [rent.customer for rent in Rent.objects.all()]
        available_customers = [(customer.id, customer.name) for customer in Customer.objects.all() if customer not in rented_customers]
        self.fields['input_customer'].choices = available_customers
