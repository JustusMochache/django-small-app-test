from django.shortcuts import render

from django.http import HttpResponse

from .models import *

# Create your views here.

def index(request):
    

    list = List.objects.all()

    context = { 'list' :list}



    return  render(request, 'smallapp/list.html', context)
