from django.shortcuts import render, redirect
from .models import Car, Customer
from .forms import CarForm, CustomerForm
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'rentacar_app/index.html', context)

def customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'rentacar_app/customers.html', context)

def customers_register(request):
    form = CustomerForm()
    context = {'form': form}

    if request.method == 'POST' and request.POST['customer_id']:
        customer = Customer.objects.get(pk=request.POST['customer_id'])
        context['customer_id'] = request.POST['customer_id']
        form.initial = {'input_name': customer.name, 'input_birthday': customer.birthday,
                        'input_cpf': customer.cpf}
        form.input_id = customer.pk

    return render(request, 'rentacar_app/customers_register.html', context)

def customers_remove(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        customer = Customer.objects.get(pk=customer_id)
        customer.delete()
        return redirect('customers')

def customer_submit(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            # TODO: Improve how we are passing the customer_id
            if request.POST['customer_id'] != 'None':
                customer = Customer.objects.get(pk=request.POST['customer_id'])
            else:
                customer = Customer()

            customer.name = form.cleaned_data['input_name']
            customer.cpf = form.cleaned_data['input_cpf']
            customer.birthday = form.cleaned_data['input_birthday']
            customer.save()

            return redirect('customers')

        else:
            return HttpResponse('Error. The form is not valid, please try again')

def cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'rentacar_app/cars.html', context)

def cars_remove(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car = Car.objects.get(pk=car_id)
        car.delete()
        return redirect('cars')

def cars_register(request):
    form = CarForm()
    context = {'form': form}

    if request.method == 'POST' and request.POST['car_id']:
        car = Car.objects.get(pk=request.POST['car_id'])
        context['car_id'] = request.POST['car_id']
        form.initial = {'input_model': car.model, 'input_plate': car.plate,
                        'input_brand': car.brand, 'input_color': car.color, 'input_price': car.price_per_day}
        form.input_id = car.pk

    return render(request, 'rentacar_app/cars_register.html', context)

def car_submit(request):
    if request.method == 'POST':
        form = CarForm(request.POST)

        if form.is_valid():
            # TODO: Improve how we are passing the customer_id
            if request.POST['car_id'] != 'None':
                car = Car.objects.get(pk=request.POST['car_id'])
            else:
                car = Car()

            car.plate = form.cleaned_data['input_plate']
            car.model = form.cleaned_data['input_model']
            car.brand = form.cleaned_data['input_brand']
            car.color = form.cleaned_data['input_color']
            car.price_per_day = float(form.cleaned_data['input_price'])
            car.save()

            return redirect('cars')
        else:
            return HttpResponse('Error. The form is not valid, please try again')