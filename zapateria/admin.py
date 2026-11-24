from django.contrib import admin
from .models import Categoria, Marca, Producto, Venta


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('nombre',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen')
    search_fields = ('nombre', 'pais_origen')
    list_filter = ('pais_origen',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'categoria', 'precio', 'stock', 'genero', 'fecha_ingreso')
    list_filter = ('genero', 'categoria', 'marca', 'fecha_ingreso')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'fecha_ingreso'


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_venta', 'cantidad_productos')
    list_filter = ('fecha_venta',)
    search_fields = ('cliente',)
    filter_horizontal = ('productos',)
    date_hierarchy = 'fecha_venta'

    def cantidad_productos(self, obj):
        return obj.productos.count()
    cantidad_productos.short_description = 'Nº productos'
