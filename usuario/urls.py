from django.urls import path,include
from rest_framework import routers
from usuario import views


router_user = routers.DefaultRouter()
router_user.register(r'usuarioP', views.profView, 'prof')

router_admin = routers.DefaultRouter()
router_admin.register(r'usuarioA', views.adminView, 'usadm')

urlpatterns = [
    path('', views.test, name='signup'),
    path('usadm/',include(router_admin.urls)),
    path('profesor/',include(router_user.urls)),
    
]
  