from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.decorators.http import require_POST
from zapateria.forms import RegistroForm


def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cuenta creada correctamente. Ya puedes usar el sistema.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'zapateria/auth/registro.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'zapateria/auth/login.html'
    redirect_authenticated_user = True


@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada.')
    return redirect('home')
