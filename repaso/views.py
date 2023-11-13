from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FechasForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        formulario = FechasForm(request.POST)
        if formulario.is_valid():
            # Procesa los datos del formulario aquí
            # Accede a los datos utilizando formulario.cleaned_data
            fecha_inicio = formulario.cleaned_data['fecha_inicio']
            fecha_fin = formulario.cleaned_data['fecha_fin']
            dias_semana = formulario.cleaned_data['dias_semana']
            email = formulario.cleaned_data['email']

            # Redirige a la página de inicio (index.html) mostrando los datos
            return render(request, 'repaso/index.html',
                          {'formulario': formulario})
    else:
        formulario = FechasForm()

    return render(request, 'repaso/index.html', {'formulario': formulario})
