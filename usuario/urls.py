from django.urls import path,include
from rest_framework import routers
from usuario.views import SignUpUserAPI, SignUpAdminAPI, UserView,AdminView

router_Prof = routers.DefaultRouter()
router_Prof.register(r'usuarioP', UserView, 'prof')

router_admin = routers.DefaultRouter()
router_admin.register(r'usuarioA', AdminView, 'admin')

urlpatterns = [

    path('signUpAdmin/', SignUpAdminAPI.as_view(), name='signUpAdmin'),
    path('SignUpUser/', SignUpUserAPI.as_view(), name='SignUpUser'),
    path('ProfList/',include(router_Prof.urls)),
    path('AdminList/',include(router_admin.urls)),
    
]
  