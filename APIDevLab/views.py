import os

from django.conf import settings
from django.views.static import serve
from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    context = {
        'variable1': 'Valor de la variable 1',
        'variable2': 'Valor de la variable 2',
    }
    
    return render(request, "index.html", context)
