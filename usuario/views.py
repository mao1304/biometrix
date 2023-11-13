from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import connection

from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,AdminSerializer, LoginSerializer
from .models import NewUser
from .forms import AdminUserForm, NewUserForm,LoginUserForm


def consulta_mysql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT curso.ciclo as ciclo,clase.curso_id,programa.info_programa,curso.grupo, curso.descripcion, DATE_FORMAT(hora_inicio, '%H:%i') AS 'hora de inicio',DATE_FORMAT(hora_fin, '%H:%i') AS 'hora de fin', clase.tema, clase.aula_id as aula, curso.num_clases_rest as 'num clases vistas', aula.numero as Aula from curso_clase as clase inner join curso_curso as curso on clase.curso_id = curso.id_curso inner join curso_programa as programa on curso.programa_id = programa.idprograma inner join curso_aula as aula on aula.idaula = clase.aula_id;")
        resultados = cursor.fetchall()
    return render(request, 'home.html', {'resultados': resultados})


class ReadOnlyUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
    
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return NewUser.objects.filter(admin_check=False)  
    permission_classes = [ReadOnlyUserPermission]

class AdminView(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    def get_queryset(self):
        return NewUser.objects.filter(admin_check=True)  
    permission_classes = [ReadOnlyUserPermission]

@method_decorator(csrf_exempt, name='dispatch')
class SignUpAdminAPI(APIView):
    def post(self, request, format=None):
        print("Entrando a la vista SignUpAdminAPI")
        form = AdminUserForm(request.data)
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

                response = Response({'message': 'Registro exitoso'}, status=status.HTTP_201_CREATED)
                response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000"
                return response
            except IntegrityError as e:
                print(f"Error de integridad: {e}")
                return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Formulario no válido")
            print("Datos del formulario:", request.data)
            return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(csrf_exempt, name='dispatch')
class SignUpUserAPI(APIView):
    def post(self, request, format=None):
        print("Entrando a la vista SignUpUserAPI")
        form = NewUserForm(request.data)
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

                response = Response({'message': 'Registro exitoso'}, status=status.HTTP_201_CREATED)
                response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000"
                return response
            except IntegrityError as e:
                print(f"Error de integridad: {e}")
                return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Formulario no válido")
            print("Datos del formulario:", request.data)
            return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)


def home_view(request):
    return render(request, 'registrer.html')

   
@method_decorator(csrf_exempt, name='dispatch')
class SignInAPI(APIView):
    # def get(self, request, format=None):
    #     form = LoginUserForm()  
    #     return render(request, 'login_template.html', {'form': form})
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            try:
                username = serializer.validated_data['username']
                password = serializer.validated_data['password']

                user = authenticate(request, username=username, password=password)

                if user is None:
                    raise SuspiciousOperation("Usuario o contraseña incorrectos.")

                login(request, user)

                return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK) 

            except SuspiciousOperation as e:
                request.session['login_attempts'] = request.session.get('login_attempts', 0) + 1
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')

class SignOutAPI(APIView):
    def post(self, request, format=None):
        request.session.flush()
        logout(request)
        return Response({'message': 'Cierre de sesión exitoso'}, status=status.HTTP_200_OK)
    
