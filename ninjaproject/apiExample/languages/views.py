from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Paradigm,Programer 
from .serializers import LanguageSerializer, ParadigmSerializer,ProgramerSerializer
  

class LanguageView(viewsets.ModelViewSet):
      queryset = Language.objects.all()
      serializer_class = LanguageSerializer
      # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class ParadigmView(viewsets.ModelViewSet):
      queryset = Paradigm.objects.all()
      serializer_class = ParadigmSerializer
      # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class ProgramerView(viewsets.ModelViewSet):
      queryset = Programer.objects.all()
      serializer_class = ProgramerSerializer
      # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)