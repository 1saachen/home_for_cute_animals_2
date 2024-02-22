from rest_framework import serializers
from .models import UserRegister


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model=UserRegister
        fields = ['id','username','password','email']
