from rest_framework import viewsets
from .serializer import  UserSerializer
from .models import  NewUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import AdminUserForm, NewUserForm, LoginUserForm
from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from rest_framework import viewsets
from .forms import AdminUserForm
from .models import NewUser


#retorna todos los registros de usuarios como json  
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = NewUser.objects.all()
    
#registro de un nuevo admnistrador e inicio de sesion del mismo
def signUpAdmin(request):
    if request.method == 'GET':
        return render(request, 'registrer.html', {"form": AdminUserForm})

    elif request.method == 'POST':
        form = AdminUserForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                admin_check = form.cleaned_data.get('admin_check', False)

                user = NewUser.objects.create_user(
                    username=username,
                    password=password,
                    admin_check=admin_check,
                )

                authenticated_user = authenticate(request, username=username, password=password)
                login(request, authenticated_user)

                return redirect(reverse('home'))

            except IntegrityError:
                return render(request, 'registrer.html', {"form": AdminUserForm, "error": "Username already exists."})
            
@login_required  
def home_view(request):
    return render(request, 'home.html')

def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'forms.html', {"form": NewUserForm})

    elif request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                huella = form.cleaned_data['huella']
                admin_check = form.cleaned_data.get('admin_check', False)

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
        username = request.POST['username']
        password = request.POST['password']
        
        # Validación del número de intentos de inicio de sesión
        if request.session.get('login_attempts', 0) >= 5:
            raise SuspiciousOperation("Número máximo de intentos de inicio de sesión alcanzado.")

        user = authenticate(request, username=username, password=password)
        if user is None:
            # Incrementar el contador de intentos de inicio de sesión
            request.session['login_attempts'] = request.session.get('login_attempts', 0) + 1
            return render(request, 'registrer.html', {"form": LoginUserForm, "error": "Username or password is incorrect."})

        # Restablecer el contador de intentos de inicio de sesión exitoso
        request.session['login_attempts'] = 0

        login(request, user)
        return redirect('home')

    # if request.method == 'GET':
    #     return render(request, 'registrer.html', {"form": LoginUserForm})

    # else:
    #     user = authenticate(
    #         request, username=request.POST['username'], password=request.POST['password'])
    #     if user is None:
    #         return render(request, 'signin.html', {"form": LoginUserForm, "error": "Username or password is incorrect."})
    #     login(request, user)
    #     return redirect('home')
    
