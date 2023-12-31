from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.http import HttpResponse

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

from curso.forms import createPrograma,updateProgrma,createCurso,createAula,creatClase
from curso.models import Programa

def generarTabla(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT curso.ciclo as ciclo,clase.curso_id,programa.info_programa,curso.grupo, curso.descripcion, DATE_FORMAT(hora_inicio, '%H:%i') AS 'hora de inicio',DATE_FORMAT(hora_fin, '%H:%i') AS 'hora de fin', clase.tema, clase.aula_id as aula, curso.num_clases_vistas as 'num clases vistas', aula.descripcion as Aula,clase.profesor_ID_id as profesor from curso_clase as clase inner join curso_curso as curso on clase.curso_id = curso.id_curso inner join curso_programa as programa on curso.programa_id = programa.idprograma inner join curso_aula as aula on aula.idaula = clase.aula_id;")
        resultados = cursor.fetchall()
    return render(request, 'consulta.html', {'resultados': resultados})

def consultarClasesProf(request, idprof):
    with connection.cursor() as cursor:
        try:
            cursor.callproc('clasesprof', args=(idprof,))  
            for result in cursor.stored_results():
                rows = result.fetchall()
        finally:
            cursor.close()
            
    return render(request, 'list.html', {'resultado': rows})



class ReadOnlyUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']  
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return NewUser.objects.filter(is_staff=False)  
    permission_classes = [ReadOnlyUserPermission]

class AdminView(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    def get_queryset(self):
        return NewUser.objects.filter(is_staff=True)  
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
    

def logIn(request):
    if request.method == 'GET':
        form = LoginUserForm()  
        return render(request, 'login_template.html', {'form': form})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            form = LoginUserForm()  
            return render(request, 'login_template.html', {"form": form, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('mainPage')

@login_required
def signout(request):
    logout(request)
    return redirect('login')

@login_required
def mainPage(request):
    if request.method == 'GET':
        return render(request, 'mainPage.html')
    
#views de el crud de programa 
def progrmas(request):
    if request.method == 'GET':
        return render(request, 'programa.html')

def editarprogrmas(request):
    idprograma = request.GET.get('idprograma')
    return render(request, 'editarprogrma.html', {'idprograma': idprograma, 'form': updateProgrma})

def crearPrograma(request):
    if request.method == 'GET':
        form = createPrograma()
        return render(request, 'agregarprograma.html', {'form': form})
    
    elif request.method == 'POST':
        form = createPrograma(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Programa creado con éxito.'
            return render(request, 'agregarprograma.html', {'form': createPrograma(), 'mensaje': mensaje})
        else:
            return render(request, 'agregarprograma.html', {'form': form})

#views de el crud de curso 
def curso(request):
    if request.method == 'GET':
        return render(request, 'curso.html')

def editarcurso(request):
    id_curso = request.GET.get('id_curso')
    return render(request, 'cursoEditar.html', {'id_curso': id_curso, 'form': createCurso})

def crearcurso(request):
    if request.method == 'GET':
        form = createCurso()
        return render(request, 'cursoCrear.html', {'form': form})
    
    elif request.method == 'POST':
        form = createCurso(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Programa creado con éxito.'
            return render(request, 'cursoCrear.html', {'form': createCurso(), 'mensaje': mensaje})
        else:
            return render(request, 'cursoCrear.html', {'form': form})

#views de el crud de aula
def aula(request):
    if request.method == 'GET':
        return render(request, 'aula.html')

def editaraula(request):
    id_curso = request.GET.get('id_curso')
    return render(request, 'aulaEditar.html', {'id_curso': id_curso, 'form': createAula})

def agregaraula(request):
    if request.method == 'GET':
        form = createAula()
        return render(request, 'aulaCrear.html', {'form': form})
    
    elif request.method == 'POST':
        form = createAula(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Programa creado con éxito.'
            return render(request, 'aulaCrear.html', {'form': createAula(), 'mensaje': mensaje})
        else:
            return render(request, 'aulaCrear.html', {'form': form})

#views de el crud de clase
def clase(request):
    if request.method == 'GET':
        return render(request, 'clase.html')

def editarclase(request):
    id = request.GET.get('id')
    return render(request, 'claseEditar.html', {'id': id, 'form': creatClase})

def agregarclase(request):
    if request.method == 'GET':
        form = creatClase()
        return render(request, 'claseCrear.html', {'form': form})
    
    elif request.method == 'POST':
        form = creatClase(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Programa creado con éxito.'
            return render(request, 'aulaCrear.html', {'form': creatClase(), 'mensaje': mensaje})
        else:
            return render(request, 'aulaCrear.html', {'form': form})