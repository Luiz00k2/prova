from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/criar_livro.html', {'form': form})

def editar_livro(request, id_livro):
    livro = Livro.objects.get(id_livro=id_livro)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/editar_livro.html', {'form': form})

def excluir_livro(request, id_livro):
    livro = Livro.objects.get(id_livro=id_livro)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livros/excluir_livro.html', {'livro': livro})