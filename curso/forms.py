from django import forms
from .models import Programa, Curso,Aula, Clase

class updateProgrma(forms.ModelForm):
    class Meta:
        model = Programa
        fields = {'info_programa', 'facultad', 'jefe_programa',}
        
class createPrograma(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'
        
class createCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        
class createAula(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'
        
class creatClase(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'