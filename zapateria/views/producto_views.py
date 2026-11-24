from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from zapateria.models import Producto
from zapateria.forms import ProductoForm


def producto_list(request):
    productos = Producto.objects.select_related('categoria', 'marca').all()
    return render(request, 'zapateria/productos/lista.html', {'productos': productos})


def producto_detail(request, pk):
    producto = get_object_or_404(Producto.objects.select_related('categoria', 'marca'), pk=pk)
    return render(request, 'zapateria/productos/detalle.html', {'producto': producto})


@login_required
@permission_required('zapateria.add_producto', raise_exception=True)
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'zapateria/productos/formulario.html', {'form': form, 'titulo': 'Nuevo producto'})


@login_required
@permission_required('zapateria.change_producto', raise_exception=True)
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('producto_detail', pk=pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'zapateria/productos/formulario.html', {'form': form, 'titulo': 'Editar producto'})


@login_required
@permission_required('zapateria.delete_producto', raise_exception=True)
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('producto_list')
    return render(request, 'zapateria/productos/confirmar_eliminar.html', {'producto': producto})
