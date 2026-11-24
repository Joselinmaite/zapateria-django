from django.urls import path
from zapateria.views import marca_views

urlpatterns = [
    path('', marca_views.marca_list, name='marca_list'),
    path('<int:pk>/', marca_views.marca_detail, name='marca_detail'),
    path('nueva/', marca_views.marca_create, name='marca_create'),
    path('<int:pk>/editar/', marca_views.marca_update, name='marca_update'),
    path('<int:pk>/eliminar/', marca_views.marca_delete, name='marca_delete'),
]
