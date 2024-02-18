from rest_framework import serializers
from .models import AdoptionRequest
from apps.pets.models import Pet
from apps.users.models import User


class AdoptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    pet = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all())

    class Meta:
        model = AdoptionRequest
        fields = ['id',
                  'user',
                  'pet',
                  'request_date',
                  'status']
        read_only_fields = ['id',
                            'request_date']

    def create(self, validated_data):
        user = validated_data.pop('user')
        pet = validated_data.pop('pet')
        instance = AdoptionRequest.objects.create(user=user, pet=pet, **validated_data)
        return instance

    def update(self, instance, validated_data):
        user = validated_data.get('user', instance.user)
        pet = validated_data.get('pet', instance.pet)
        instance.user = user
        instance.pet = pet
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
