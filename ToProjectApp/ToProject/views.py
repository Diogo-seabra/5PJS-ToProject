from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import importlib.util
from .forms import CriarProjetoForm
from django.views.generic import ListView, DetailView, UpdateView
from .models import Projeto, Tarefa
from django.forms import inlineformset_factory
# Create your views here.

TarefaFormSet = inlineformset_factory(
    Projeto,  # Modelo pai
    Tarefa,   # Modelo relacionado
    fields=['nome', 'status', 'prioridade', 'responsavel'],  # Campos do formulário de Tarefa
    extra=1,  # Quantidade de formulários vazios adicionais para novas tarefas
    can_delete=True  # Permitir exclusão de tarefas existentes
)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = TarefaFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = TarefaFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('ver_projeto', kwargs={'pk': self.object.pk})


class Ver_projeto(DetailView):
    template_name = "ver_projeto.html"
    model = Projeto
