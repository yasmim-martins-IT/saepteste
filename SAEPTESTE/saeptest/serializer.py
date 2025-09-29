from rest_framework import serializers
from .models import Usuario , Tarefa


class UsuarioSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Usuario
        fields ='__all__' 

from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    prioridade = serializers.CharField(source="get_prioridade_display", read_only=True)
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Tarefa
        fields = ["id", "descricao", "setor", "prioridade", "status", "usuario", "data_criacao"]
