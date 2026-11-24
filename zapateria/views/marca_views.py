from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from zapateria.models import Marca
from zapateria.forms import MarcaForm


def marca_list(request):
    marcas = Marca.objects.all()
    return render(request, 'zapateria/marcas/lista.html', {'marcas': marcas})


def marca_detail(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    return render(request, 'zapateria/marcas/detalle.html', {'marca': marca})


@login_required
@permission_required('zapateria.add_marca', raise_exception=True)
def marca_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca creada correctamente.')
            return redirect('marca_list')
    else:
        form = MarcaForm()
    return render(request, 'zapateria/marcas/formulario.html', {'form': form, 'titulo': 'Nueva marca'})


@login_required
@permission_required('zapateria.change_marca', raise_exception=True)
def marca_update(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca actualizada correctamente.')
            return redirect('marca_detail', pk=pk)
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'zapateria/marcas/formulario.html', {'form': form, 'titulo': 'Editar marca'})


@login_required
@permission_required('zapateria.delete_marca', raise_exception=True)
def marca_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        messages.success(request, 'Marca eliminada correctamente.')
        return redirect('marca_list')
    return render(request, 'zapateria/marcas/confirmar_eliminar.html', {'marca': marca})
