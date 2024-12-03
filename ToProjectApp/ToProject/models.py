from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

LISTA_COR = [
    ("VERDE", "Verde"),
    ("AMARELO", "Amarelo"),
    ("VERMELHO", "Vermelho")
]

LISTA_STATUS = [
    ("NAO_CONCLUIDO", "Em producao"),
    ("CONCLUIDO", "Concluido")
]

LISTA_PRIORIDADE = [
    ("ALTA", "Alta"),
    ("MEDIA", "Media"),
    ("BAIXA", "Baixa")
]

class Usuario(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Nome único para evitar conflitos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Nome único para evitar conflitos
        blank=True
    )

class Projeto(models.Model):
    nome = models.CharField(max_length=30)
    dataInicio = models.DateField()
    dataFinal = models.DateField()
    descricao = models.TextField(max_length=1000)
    responsavel = models.CharField(max_length=30)
    cor = models.CharField(max_length=15, choices=LISTA_COR)
    tag = models.CharField(max_length=15)
    status_projeto = models.CharField(max_length=15, choices=LISTA_STATUS)
    cliente = models.CharField(max_length=30)

    def str(self):
        return self.nome


class Tarefa(models.Model):
    nome = models.CharField(max_length=30)
    status = models.CharField(max_length=15, choices=LISTA_STATUS)
    prioridade = models.CharField(max_length=15, choices=LISTA_PRIORIDADE)
    responsavel = models.CharField(max_length=30)
    projeto = models.ForeignKey("Projeto", on_delete=models.CASCADE, related_name="tarefas")

    def str(self):
        return self.nome