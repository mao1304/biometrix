from django.urls import path,include
from rest_framework import routers
from curso import views


router1 = routers.DefaultRouter()
router = routers.DefaultRouter()
router1.register(r'clase', views.claseView, 'clase')
router.register(r'aula', views.aulaView, 'aula')
router.register(r'programa', views.programaView, 'programa')
router.register(r'curso', views.cursoView, 'curso')

urlpatterns = [
    path('clase/',include((router1.urls))),
    path('aula/',include(router.urls)),
 
]
  