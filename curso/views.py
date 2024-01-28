from rest_framework import viewsets,status
from rest_framework.views import APIView
from curso import serializer as serializerCurso
from curso import models as ModelsCurso
from django.shortcuts import render 
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class aulaView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.AulaSerializer
    queryset = ModelsCurso.Aula.objects.all()
        
class programaView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.ProgramaSerializer
    queryset = ModelsCurso.Programa.objects.all()
       
class claseView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.ClaseSerializer
    queryset = ModelsCurso.Clase.objects.all()
      
class cursoView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.CursoSerializer
    queryset = ModelsCurso.Curso.objects.all()
    