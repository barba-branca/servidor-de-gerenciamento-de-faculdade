from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Professor, Estudante
from .forms import CursoForm, ProfessorForm, EstudanteForm

# Cliente

def list_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'core/list_cursos.html', {'cursos': cursos})

def novo_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_curso')
    else:
        form = CursoForm()
    return render(request, 'core/form_curso.html', {'form': form})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso,pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_vaslid():
            form.save()
            return redirect('lista_cursos')
        else:
         form = CursoForm(instance=curso)
    return render(request, 'core/form_cuso.html', {'form': form})

def deletar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'core/condirmar_delete.html', {'obj': curso})

#Professores
def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'core/lista_professores.html', {'professores': professores})

def novo_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_professores')
    else:
        form = ProfessorForm()
    return render(request,'core/form_professor.html', {'form': form})

def editar_professor(request, pk):
    professor = get_object_or_404(professor,pk= pk)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('lista_professores')
        else:
            form = ProfessorForm(instace=professor)
            return render(request, 'core/form_professor.html', {'form': form})
        
def editar_professoe(request, pk):
    professor = get_object_or_404(professor, pk=pk)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('lista_professores')
        else:
            form = ProfessorForm(instace=professor)
        return render(request,'core/form_professor.html',{'form': form})
    
def deletar_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('lista_professores')
    return render(request, 'core/confirmar_delete.html',{'obj': professor})

# Estudades

def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'core/lista_estudante.html', {'estudantes': estudantes})

def novo_estudates(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudante')
    else:
        form = EstudanteForm()
    return render(request, 'core/form_estudante.html', {'form': form})

def editar_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    if request.method == 'POST':
        form = EstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()    
            return redirect('lista_estudante')
    else:
        form = EstudanteForm(instance=estudante)
    return render(request, 'core/form_estudante.html', {'form': form})
    
def deletar_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    if request.method == 'POST':
        estudante.delete()
        return redirect('lista_estudante')
    return render(request, 'core/confirmar_delete.html', {'obj': estudante})