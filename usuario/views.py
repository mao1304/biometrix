from rest_framework import viewsets
from .serializer import adminserializer, profesorserializer
from .models import Usuadm, Profesor

class adminView(viewsets.ModelViewSet):
    serializer_class = adminserializer
    queryset = Usuadm.objects.all()
    
class profView(viewsets.ModelViewSet):
    serializer_class = profesorserializer
    queryset = Profesor.objects.all()