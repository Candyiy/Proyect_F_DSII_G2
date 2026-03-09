from django import forms
<<<<<<< HEAD
from .models import Educacion, Servicio, Habilidad
=======
from .models import Educacion
>>>>>>> 5f3ae44d9e6ece5b9db81cfaac1b3de8adf6f898

class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
<<<<<<< HEAD
        fields = ['titulo', 'institucion', 'año_finalizacion', 'descripcion']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'categoria', 'disponible']


NIVELES = [
    ('Basico', 'Básico'),
    ('Intermedio', 'Intermedio'),
    ('Avanzado', 'Avanzado'),
    ('Experto', 'Experto'),
]

class HabilidadForm(forms.ModelForm):
    nivel = forms.ChoiceField(choices=NIVELES)

    class Meta:
        model = Habilidad
        fields = ['nombre', 'nivel', 'descripcion']
=======
        fields = ['titulo', 'institucion', 'año_finalizacion', 'descripcion']
>>>>>>> 5f3ae44d9e6ece5b9db81cfaac1b3de8adf6f898
