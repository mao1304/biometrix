from rest_framework import serializers
from .models import NewUser



     
class profesorserializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields= '__all__'