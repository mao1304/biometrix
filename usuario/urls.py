from django.urls import path,include
from rest_framework import routers
from usuario import views
from curso.views import ProgramaView
 
router_Prof = routers.DefaultRouter()
router_Prof.register(r'usuarioP', views.UserView, 'prof')

router_admin = routers.DefaultRouter()
router_admin.register(r'usuarioA', views.AdminView, 'admin')

urlpatterns = [
    #API views
    path('signUpAdmin/', views.SignUpAdminAPI.as_view(), name='signUpAdmin'),
    path('SignUpUser/', views.SignUpUserAPI.as_view(), name='SignUpUser'),
    path('SignInAPI/', views.SignInAPI.as_view(), name='SignInAPI'),
    path('logout/', views.SignOutAPI.as_view(), name='logoutAPI'),
    path('ProfList/',include(router_Prof.urls)),
    path('AdminList/',include(router_admin.urls)),
    
    #web views 
    path('',views.logIn, name='login'),
    path('generarTabla',views.generarTabla, name='generarTabla'),
    path('signout/',views.signout, name='signout'),
    path('mainPage/',views.mainPage, name='mainPage'),
    #view crud programa
    path('programas/',views.progrmas, name='programas'),
    path('editarprogramas/', views.editarprogrmas, name='editarprogramas'),
    path('agregarprogramas/', views.crearPrograma, name='agregarprogramas'),
    #view crud curso
    path('curso/',views.curso, name='curso'),
    path('editarcurso/', views.editarcurso, name='editarcurso'),
    path('agregarcurso/', views.crearcurso, name='agregarcurso'),
    #view crud aula
    path('aula/',views.aula, name='aula'),
    path('editaraula/', views.editaraula, name='editaraula'),
    path('agregaraula/', views.agregaraula, name='agregaraula'),
    #view crud clases
    path('clases/',views.clase, name='clase'),
    path('editarclase/', views.editarclase, name='editarclase'),
    path('agregarclase/', views.agregarclase, name='agregarclase'),
    #view crud usuarios
    path('usuarios/',views.aula, name='aula'),
    path('editaraula/', views.editaraula, name='editaraula'),
    path('agregaraula/', views.agregaraula, name='agregaraula'),
    
    path('consultarlista/', views.consultarClasesProf , name='consultarClasesProf'),
    
]
  