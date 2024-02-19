from rest_framework import serializers
from .models import AdoptionRequest
from users.models import User
from pets.models import Pet
from users.serializers import UserProfileSerializer
from pets.serializers import PetSerializer
class AdoptionSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    pet = PetSerializer(read_only=True)

    class Meta:
        model = AdoptionRequest
        fields = ['id',
                  'user',
                  'pet',
                  'adoption_date',
                  'status']
        read_only_fields = ['id',
                            'adoption_date']

    class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id',
                      'real_name']

    class PetSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pet
            fields = ['id',
                      'name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        pet_data = validated_data.pop('pet')

        user = User.objects.get(id=user_data['id'])
        pet = Pet.objects.get(id=pet_data['id'])

        instance = AdoptionRequest.objects.create(user=user, pet=pet, **validated_data)
        return instance

    def update(self, instance, validated_data):
        # 不管用户和宠物的更新
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance