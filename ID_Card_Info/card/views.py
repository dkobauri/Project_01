from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *

def home(request):
    info = Information.objects.all()
    return render(request, 'card/info.html', {'list':info})