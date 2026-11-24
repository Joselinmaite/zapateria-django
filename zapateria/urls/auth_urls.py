from django.urls import path
from zapateria.views.auth_views import registro, CustomLoginView, logout_view

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
