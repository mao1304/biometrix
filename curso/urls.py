from django.urls import path,include
from rest_framework import routers
from curso import views

app_name = 'curso'

router_clase = routers.DefaultRouter()
router_clase.register(r'clase', views.claseView, 'clase')

router_aula = routers.DefaultRouter()
router_aula.register(r'aula', views.aulaView, 'aula')

router_programa = routers.DefaultRouter()
router_programa.register(r'programa', views.programaView)

router_curso = routers.DefaultRouter()
router_curso.register(r'curso', views.cursoView, 'curso')

urlpatterns = [
    path('clase/',include(router_clase.urls)),
    path('aula/',include(router_aula.urls)),
    path('programa/',include(router_programa.urls)),
    path('curso/',include(router_curso.urls)),
 
]
