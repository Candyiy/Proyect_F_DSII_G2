from django.shortcuts import render, redirect

# Create your views here.

from .forms import EducacionForm
from job.models import OfertaLaboral


def home(request):
    ofertas = OfertaLaboral.objects.all().order_by('-fecha_publicacion')
    return render(request, "pages/home.html", {'ofertas': ofertas})

def job(request):
    ofertas = OfertaLaboral.objects.all().order_by('-fecha_publicacion')
    return render(request, "pages/job.html", {'ofertas': ofertas})

def mensajes(request):
    return render(request, "pages/mensajes.html")

def listapostulantes(request):
    return render(request, "pages/listapostulantes.html")

def profile(request):
    # mostrar formulario de educación y procesar envíos
    if request.method == 'POST':
        form = EducacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EducacionForm()
    return render(request, "pages/profile.html", {"form": form})