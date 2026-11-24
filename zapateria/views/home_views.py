from django.shortcuts import render
from zapateria.models import Producto, Venta, Categoria, Marca


def home(request):
    context = {
        'total_productos': Producto.objects.count(),
        'total_ventas': Venta.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'total_marcas': Marca.objects.count(),
    }
    return render(request, 'zapateria/home.html', context)
