from django import forms
from .models import Educacion, Servicio, Habilidad

class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
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