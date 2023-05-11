from django.db import models
from rest_framework import serializers


class Data(models.Model):
    data = models.TextField()


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['data']
