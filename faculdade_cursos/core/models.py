from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome