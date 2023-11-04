from rest_framework import serializers
from .models import AdminUser, NormalUser


class adminserializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields= '__all__'
        
class profesorserializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields= '__all__'