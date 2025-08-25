from rest_framework import serializers
from models import Usuario , Tarefa


class UsuarioSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Usuario
        fields ='__all__' 