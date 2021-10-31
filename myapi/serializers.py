from django.db import models
from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias', 'age', "id")
