from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import importlib.util
from .forms import CriarProjetoForm
from django.views.generic import ListView, DetailView, UpdateView
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

class Editar_projeto(UpdateView):
    template_name = "editar_projeto.html"
    model = Projeto
    fields = ['nome', 'dataInicio', 'dataFinal', 'descricao', 'responsavel', 'cor', 'tag', 'status_projeto', 'cliente']

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self):
        return reverse('Home')


class Ver_projeto(DetailView):
    template_name = "ver_projeto.html"
    model = Projeto
