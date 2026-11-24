from django.urls import path
from zapateria.views import producto_views

urlpatterns = [
    path('', producto_views.producto_list, name='producto_list'),
    path('<int:pk>/', producto_views.producto_detail, name='producto_detail'),
    path('nuevo/', producto_views.producto_create, name='producto_create'),
    path('<int:pk>/editar/', producto_views.producto_update, name='producto_update'),
    path('<int:pk>/eliminar/', producto_views.producto_delete, name='producto_delete'),
]
