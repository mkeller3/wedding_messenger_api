from rest_framework import serializers
from .models import *

class accountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountData
        fields = '__all__'

class guestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = guestData
        fields = '__all__'

class groupDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = groupData
        fields = '__all__'

class alertDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = alertData
        fields = '__all__'

class trialNumberDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = trialNumberData
        fields = '__all__'