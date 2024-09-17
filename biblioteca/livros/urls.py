from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('criar/', views.criar_livro, name='criar_livro'),
    path('editar/<int:id_livro>/', views.editar_livro, name='editar_livro'),
    path('excluir/<int:id_livro>/', views.excluir_livro, name='excluir_livro'),
]
