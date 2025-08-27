from django.shortcuts import render
from django.http import HttpRequest 
from models import Usuario , Tarefa
from rest_framework import status 
from serializer import TarefaSerializer , UsuarioSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import serializers
# Create your views here.

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    def get_queryset(self) :
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        serie = self.request.query_params.get('serie')


        if nome :
            queryset = queryset.filter(nome__icontains = nome)
        elif serie :
            queryset = queryset.filter(serie__icontains = serie)
        return queryset
    def perform_create(self, serializer):
        serializer.save()

class TarefaListCreateAPIView(ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


    def get_queryset(self) :
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        serie = self.request.query_params.get('serie')


        if nome :
            queryset = queryset.filter(nome__icontains = nome)
        elif serie :
            queryset = queryset.filter(serie__icontains = serie)
        return queryset
    def perform_create(self, serializer):
        serializer.save()



class TarefaRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    lookup_field = 'pk'