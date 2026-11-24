from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from zapateria.models import Categoria
from zapateria.forms import CategoriaForm


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'zapateria/categorias/lista.html', {'categorias': categorias})


def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'zapateria/categorias/detalle.html', {'categoria': categoria})


@login_required
@permission_required('zapateria.add_categoria', raise_exception=True)
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'zapateria/categorias/formulario.html', {'form': form, 'titulo': 'Nueva categoría'})


@login_required
@permission_required('zapateria.change_categoria', raise_exception=True)
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente.')
            return redirect('categoria_detail', pk=pk)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'zapateria/categorias/formulario.html', {'form': form, 'titulo': 'Editar categoría'})


@login_required
@permission_required('zapateria.delete_categoria', raise_exception=True)
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
        return redirect('categoria_list')
    return render(request, 'zapateria/categorias/confirmar_eliminar.html', {'categoria': categoria})
