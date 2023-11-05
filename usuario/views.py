from rest_framework import viewsets
from .serializer import  profesorserializer
from .models import  NewUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import AdminUserForm, NewUserForm, LoginAdminForm, LoginUserForm




#retorna todos los registros de usuarios como json  
class profView(viewsets.ModelViewSet):
    serializer_class = profesorserializer
    queryset = NewUser.objects.all()
    
#registro de un nuevo admnistrador e inicio de sesion del mismo
def signUpAdmin(request):
    if request.method == 'GET':
        return render(request, 'registrer.html', {"form": AdminUserForm})

    elif request.method == 'POST':
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            admin_check = request.POST.get("admin_check", False) == "on"

            user = NewUser.objects.create_user(
                username=username,
                password=password,
                admin_check=admin_check,
            )

            authenticated_user = authenticate(request, username=username, password=password)
            login(request, authenticated_user)
            user.save()
            return redirect(reverse('home'))

        except IntegrityError:
            return render(request, 'signup.html', {"form": AdminUserForm, "error": "Username already exists."})
@login_required  
def home_view(request):
    return render(request, 'home.html')

def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'forms.html', {"form": NewUserForm})

    elif request.method == 'POST':
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            huella = request.POST["huella"]
            admin_check = request.POST.get("admin_check", False) == "on"

            user = NewUser.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                huella=huella,
                admin_check=admin_check,
            )

            user.save()
            print("User saved")

        except IntegrityError:
            return render(request, 'signup.html', {"form": AdminUserForm, "error": "Username already exists."})
        
def SignIn(request):
    if request.method == 'GET':
        return render(request, 'registrer.html', {"form": LoginUserForm})

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": LoginUserForm, "error": "Username or password is incorrect."})
        login(request, user)
        return redirect('home')
    
