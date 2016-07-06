from django import forms

class CarForm(forms.Form):
    inputModel = forms.CharField(label='Model', max_length=100)
    inputPlate = forms.CharField(label='Plate', max_length=100)
    inputBrand = forms.CharField(label='Brand', max_length=100)
    inputColor = forms.CharField(label='Color', max_length=100)
    inputPrice = forms.FloatField(label='Price per day')

class CustomerForm(forms.Form):
    inputName = forms.CharField(label='Name', max_length=100)
    inputCPF = forms.CharField(label='CPF', max_length=14)
    inputBirthday = forms.DateField(label='Birthday', input_formats=['%d-%m-%Y','%d/%m/%Y', '%d/%m/%y'])
