from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class AktyorSerializer(serializers.Serializer):
    ism = serializers.CharField()
    t_sana = serializers.DateField()
    davlat = serializers.CharField()
    jins = serializers.CharField()


class KinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'

    def to_representation(self, instance):
        kino = super(KinoSerializer, self).to_representation(instance)
        soni = Izoh.objects.filter(kino__id=kino["id"]).count()
        kino.update({"izohlar_soni": soni})
        return kino


class KinoAktyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = KinoAktyor
        fields = '__all__'


class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'


class AktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'

    def to_representation(self, instance):
        aktyor = super(AktorSerializer, self).to_representation(instance)
        kinolar_soni = KinoAktyor.objects.filter(aktyor__id=aktyor.get('id')).count()
        aktyor.update({"kinolar_soni": kinolar_soni})
        return aktyor
