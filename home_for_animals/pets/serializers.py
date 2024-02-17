from rest_framework import serializers
from .models import Pet,Adoption

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'  # 或者列出所有具体字段

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ['id', 'pet', 'user', 'adopted_at', 'status']