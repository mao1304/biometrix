from rest_framework import viewsets
from .serializer import adminserializer, profesorserializer
from .models import AdminUser, NormalUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.urls import reverse
from .forms import NormalUserForm

#retorna todos los registros de admin como json
class adminView(viewsets.ModelViewSet):
    serializer_class = adminserializer
    queryset = AdminUser.objects.all()

#retorna todos los registros de profesor como json  
class profView(viewsets.ModelViewSet):
    serializer_class = profesorserializer
    queryset = NormalUser.objects.all()
    
def test(request):
    return render(request,'forms.html', {"form": NormalUserForm})

def signupAdmin(request):
    if request.method == 'GET':
        return render(request, {"form": UserCreationForm})
    elif request.method == 'POST':
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect(reverse('mainPage'))  
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('mainPage')