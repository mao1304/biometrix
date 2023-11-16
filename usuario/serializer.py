from rest_framework import serializers
from .models import NewUser

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields= ('username', 'password', 'is_staff',) 
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields= ('username', 'password', 'first_name', 'last_name','huella', 'is_staff',) 
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()