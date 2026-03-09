from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import EducacionForm
from job.models import OfertaLaboral

@login_required
def home(request):
    ofertas = OfertaLaboral.objects.all().order_by('-fecha_publicacion')
    return render(request, "pages/home.html", {'ofertas': ofertas})

@login_required
def job(request):
    ofertas = OfertaLaboral.objects.all().order_by('-fecha_publicacion')
    return render(request, "pages/job.html", {'ofertas': ofertas})

@login_required
def mensajes(request):
    return render(request, "pages/mensajes.html")

@login_required
def listapostulantes(request):
    return render(request, "pages/listapostulantes.html")

