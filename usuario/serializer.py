from rest_framework import serializers
from .models import Usuadm, Profesor


class adminserializer(serializers.ModelSerializer):
    class Meta:
        model = Usuadm
        fields= '__all__'
        
class profesorserializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields= '__all__'