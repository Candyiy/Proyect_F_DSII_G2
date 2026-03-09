from django.shortcuts import render, redirect
from .forms import OfertaForm
from .models import OfertaLaboral
<<<<<<< HEAD


=======
from django.contrib.auth.decorators import login_required

@login_required
>>>>>>> 5f3ae44d9e6ece5b9db81cfaac1b3de8adf6f898
def crear_oferta(request):

    if request.method == 'POST':
        form = OfertaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_ofertas')

    else:
        form = OfertaForm()

    return render(request, 'ofertas/formulario.html', {'form': form})

<<<<<<< HEAD

=======
@login_required
>>>>>>> 5f3ae44d9e6ece5b9db81cfaac1b3de8adf6f898
def lista_ofertas(request):

    ofertas = OfertaLaboral.objects.all()

    return render(request, 'pages/job.html', {'ofertas': ofertas})