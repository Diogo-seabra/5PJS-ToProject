from django.shortcuts import render, redirect
from django.http import HttpResponse
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import importlib.util
from .forms import CriarProjetoForm
from django.views.generic import ListView
from .models import Projeto
# Create your views here.

class Home(ListView):
    template_name = "gerencia.html"
    model = Projeto
    #return render(request,"gerencia.html",{})


def criar_projeto(request):
    if request.method == 'POST':
        form = CriarProjetoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('Home')  
    else:
        form = CriarProjetoForm()
    
    return render(request, 'criar_projeto.html', {'form': form})