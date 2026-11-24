from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from zapateria.models import Venta
from zapateria.forms import VentaForm


def venta_list(request):
    ventas = Venta.objects.prefetch_related('productos').all()
    return render(request, 'zapateria/ventas/lista.html', {'ventas': ventas})


def venta_detail(request, pk):
    venta = get_object_or_404(Venta.objects.prefetch_related('productos'), pk=pk)
    return render(request, 'zapateria/ventas/detalle.html', {'venta': venta})


@login_required
@permission_required('zapateria.add_venta', raise_exception=True)
def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta registrada correctamente.')
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'zapateria/ventas/formulario.html', {'form': form, 'titulo': 'Nueva venta'})


@login_required
@permission_required('zapateria.change_venta', raise_exception=True)
def venta_update(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada correctamente.')
            return redirect('venta_detail', pk=pk)
    else:
        form = VentaForm(instance=venta)
    return render(request, 'zapateria/ventas/formulario.html', {'form': form, 'titulo': 'Editar venta'})


@login_required
@permission_required('zapateria.delete_venta', raise_exception=True)
def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada correctamente.')
        return redirect('venta_list')
    return render(request, 'zapateria/ventas/confirmar_eliminar.html', {'venta': venta})
