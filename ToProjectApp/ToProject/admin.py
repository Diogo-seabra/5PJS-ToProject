from django.contrib import admin

#import
from django.contrib import admin
from .models import Usuario, Projeto, Tarefa

# Register your models here.




admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Tarefa)