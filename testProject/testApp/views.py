from django.shortcuts import render

# Create your views here.

from django.shortcuts import render #not used yet need templates first
from django.http import HttpResponse #testing that url routing is working?
from .models import Pet
from django.http import Http404 # needed for 404 response


def home(request):
    #perform an orm query to get all pets
    pets = Pet.objects.all()
    # call render method defining template to use
    # 'home.html and pass pets through as an argument in a dictionary
    return render(request,	'home.html', {'pets':pets,})

def pet_detail(request, pet_id): 
    try:
        # perform an ORM query to get specific pet
        pet = Pet.objects.get(id=pet_id) 
    except Pet.DoesNotExist:
        # Show an appropriate 404 message
        raise Http404("Pet not found")
    return render(request, 'pet_detail.html', {'pet':pet,})
