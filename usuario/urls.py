from django.urls import path,include
from rest_framework import routers
from usuario import views


router = routers.DefaultRouter()
router.register(r'usuarioA', views.adminView, 'usadm')
router.register(r'usuarioP', views.profView, 'prof')

urlpatterns = [
    path('usadm/',include(router.urls)),
    path('profesor/',include(router.urls)),
    
]
