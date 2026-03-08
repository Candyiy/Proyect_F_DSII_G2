from django.shortcuts import render, redirect

# Create your views here.

from .forms import EducacionForm


def home(request):
    return render(request, "pages/home.html")

def job(request):
    return render(request, "pages/job.html")

def mensajes(request):
    return render(request, "pages/mensajes.html")


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