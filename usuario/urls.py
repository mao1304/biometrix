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
    path('mainPage/',views.mainPage, name='mainPage'),
    path('programas/',views.progrmas, name='programas'),
    path('editarprogramas/', views.editarprogrmas, name='editarprogramas'),
    path('agregarprogramas/', views.crearPrograma, name='agregarprogramas'),

]
  