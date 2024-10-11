from django.shortcuts import render

# Create your views here.

from django.shortcuts import render #not used yet need templates first
from django.http import HttpResponse #testing that url routing is working?
from .models import Pet

def home(request):
    #perform an orm query to get all pets
    pets = Pet.objects.all()
    # call render method defining template to use
    # 'home.html and pass pets through as an argument in a dictionary
    return render(request,	'home.html', {'pets':pets,})

def pet_detail(request,pet_id):
    return HttpResponse(F"<h1>Pet Number: {pet_id}") 
