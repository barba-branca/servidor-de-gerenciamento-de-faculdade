from django.contrib import admin

# Register your models here.
from .models import Curso, Professor, Estudante

admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Estudante)
