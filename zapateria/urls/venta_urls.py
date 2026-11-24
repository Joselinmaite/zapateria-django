from django.urls import path
from zapateria.views import venta_views

urlpatterns = [
    path('', venta_views.venta_list, name='venta_list'),
    path('<int:pk>/', venta_views.venta_detail, name='venta_detail'),
    path('nueva/', venta_views.venta_create, name='venta_create'),
    path('<int:pk>/editar/', venta_views.venta_update, name='venta_update'),
    path('<int:pk>/eliminar/', venta_views.venta_delete, name='venta_delete'),
]
