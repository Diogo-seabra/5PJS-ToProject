from django import forms
from .models import Projeto, Tarefa


class CriarProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'dataInicio', 'dataFinal', 'descricao', 'responsavel', 'cor', 'tag', 'status_projeto', 'cliente']

        labels = {
            'nome': 'Nome do Projeto',
            'dataInicio': 'Data de Início',
            'dataFinal': 'Data Final',
            'descricao': 'Descrição do Projeto',
            'responsavel': 'Responsável pela Tarefa',
            'cor': 'Cor de Identificação',
            'tag': 'Tags Prioritárias',
            'status_projeto': 'Status do Projeto',
            'cliente': 'Cliente Associado',
        }

        widgets = {
            'dataInicio': forms.DateInput(attrs={'type': 'date'}),
            'dataFinal': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'status', 'prioridade', 'responsavel']