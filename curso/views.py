from rest_framework import viewsets,status
from rest_framework.views import APIView
from curso import serializer as serializerCurso
from curso import models as ModelsCurso
from django.shortcuts import render 
from rest_framework.response import Response

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
    
class ProgramaView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = serializerCurso.ProgramaSerializer
        return render(request, 'agregarprograma.html', {'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = serializerCurso.ProgramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)