from rest_framework import serializers
from .models import Language, Paradigm, Programer



class LanguageSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
           model = Language 
           fields = ('id','url', 'name', 'paradigm')

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
           model = Paradigm
           fields = ('id','url', 'name')
           


class ProgramerSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
           model = Programer
           fields = ('id','url', 'name', 'language')
           