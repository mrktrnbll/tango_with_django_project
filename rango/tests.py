from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.

def index(request):
    return HttpResponse("Rango says hey there partner!")

