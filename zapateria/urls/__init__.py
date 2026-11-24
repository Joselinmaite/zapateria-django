from django.urls import path, include
from zapateria.views.home_views import home

urlpatterns = [
    path('', home, name='home'),
    path('categorias/', include('zapateria.urls.categoria_urls')),
    path('marcas/', include('zapateria.urls.marca_urls')),
    path('productos/', include('zapateria.urls.producto_urls')),
    path('ventas/', include('zapateria.urls.venta_urls')),
    path('cuenta/', include('zapateria.urls.auth_urls')),
]
