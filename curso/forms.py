from django import forms
from .models import Programa

class updateProgrma(forms.ModelForm):
    class Meta:
        model = Programa
        fields = {'info_programa', 'facultad', 'jefe_programa',}
        
class createPrograma(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'