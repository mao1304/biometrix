from django.urls import path,include
from rest_framework import routers
from usuario import views


router_user = routers.DefaultRouter()
router_user.register(r'usuarioP', views.profView, 'prof')



urlpatterns = [
    path('', views.loginUser, name='loginUser'),
    path('loginAdmin', views.loginAdmin, name='loginAdmin'),
    path('home/', views.home_view, name='home'), 
    path('profesor/',include(router_user.urls)),
    
]
  