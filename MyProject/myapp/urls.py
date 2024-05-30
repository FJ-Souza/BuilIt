from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("", index, name="index"),
    path("listar/", listar, name="listarMateriais"),
    path("addMateriais/", addMaterial, name="adicionarMateriais"),
    path("editarMaterias/<int:id>", edit, name="editar_item"),
    path("atualizarMateriais/<int:id>", update, name="atualizar_item"),
    path("visualizarMaterias/<int:id>", read, name="visualizar_item"),
    path("deletarMateriais/<int:id>", delete, name="deletar_item")
]