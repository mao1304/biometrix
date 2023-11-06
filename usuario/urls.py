from django.urls import path,include
from rest_framework import routers
from usuario import views


router_user = routers.DefaultRouter()
router_user.register(r'usuarioP', views.profView, 'prof')



from django.urls import path,include
from rest_framework import routers
from usuario import views


router_user = routers.DefaultRouter()
router_user.register(r'usuarioP', views.UserView, 'prof')



urlpatterns = [
    path('', views.SignIn, name='loginUser'),
    path('signUpAdmin/', views.signUpAdmin, name='signUpAdmin'),
    path('signUpUser/', views.signUpUser, name='signUpUser'),
    path('home/', views.home_view, name='home'), 
    path('profesor/',include(router_user.urls)),
    
]
  