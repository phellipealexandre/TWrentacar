from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car

def index(request):
    context = {}
    return render(request, 'rentacar_app/index.html', context)

def customers(request):
    return HttpResponse("<h2> Hello. Welcome to the customer screen </h2>")

def cars(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, 'rentacar_app/cars.html', context)

def cars_register(request):
    context = {}
    return render(request, 'rentacar_app/cars_register.html', context)

def car_submit(request):
    if request.method == 'POST':
        model = request.POST["inputModel"]
        plate = request.POST["inputPlate"]
        brand = request.POST["inputBrand"]
        color = request.POST["inputColor"]
        price_per_day = request.POST["inputPrice"]

        car = Car()
        car.plate = plate
        car.model = model
        car.brand = brand
        car.color = color
        car.price_per_day = float(price_per_day)
        car.save()

        return redirect("cars")
