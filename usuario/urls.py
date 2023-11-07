from django.urls import path,include
from rest_framework import routers
from usuario import views

router_Prof = routers.DefaultRouter()
router_Prof.register(r'usuarioP', views.UserView, 'prof')

router_admin = routers.DefaultRouter()
router_admin.register(r'usuarioA', views.AdminView, 'admin')

urlpatterns = [

    path('signUpAdmin/', views.SignUpAdminAPI.as_view(), name='signUpAdmin'),
    path('SignUpUser/', views.SignUpUserAPI.as_view(), name='SignUpUser'),
    path('ProfList/',include(router_Prof.urls)),
    path('AdminList/',include(router_admin.urls)),
    
]
  