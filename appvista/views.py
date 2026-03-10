from django.shortcuts import render, redirect

# Create your views here.

from .forms import EducacionForm, ServicioForm, HabilidadForm
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

    educacion_form = EducacionForm()
    servicio_form = ServicioForm()
    habilidad_form = HabilidadForm()

    if request.method == 'POST':

        # FORMULARIO EDUCACION
        if 'guardar_educacion' in request.POST:
            educacion_form = EducacionForm(request.POST)
            if educacion_form.is_valid():
                educacion_form.save()
                return redirect('profile')

        # FORMULARIO SERVICIO
        elif 'guardar_servicio' in request.POST:
            servicio_form = ServicioForm(request.POST)
            if servicio_form.is_valid():
                servicio_form.save()
                return redirect('profile')

        # FORMULARIO HABILIDAD
        elif 'guardar_habilidad' in request.POST:
            habilidad_form = HabilidadForm(request.POST)
            if habilidad_form.is_valid():
                habilidad_form.save()
                return redirect('profile')

    return render(request, "pages/profile.html", {
        "educacion_form": educacion_form,
        "servicio_form": servicio_form,
        "habilidad_form": habilidad_form,
    })
