from django.shortcuts import render

from django.http import HttpResponse
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import importlib.util

# Create your views here.

def home(request):

    return render(request,"gerencia.html",{})