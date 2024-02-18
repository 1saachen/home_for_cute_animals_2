from apps.adoptions.serializers import AdoptionSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import DonationRecord, UserProfile, VolunteerRecord

class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ["__all__"]
    #
    # def validate_password(self, value):
    #     return make_password(value)
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "nickname",
            "openid",
            "union_id",
            "nick_name",
            "avatar",
            "real_name",
            "gender",
            "id_card",
            "phone",
            "email",
            "signature",
        ]
        read_only_fields = ["id", "id_card", "real_name"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class AdoptionSerializer(serializers.ModelSerializer):
    adoption_requests = AdoptionSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ["id", "real_name", "adoption_requests"]

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["adoption_requests"] = [
            request.id for request in instance.adoption_requests.all()
        ]
        return rep

class VolunteerRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerRecord
        fields = ["id",
                  "real_name",
                  "volunteer_date",
                  "activity",
                  "hours"]

class DonationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationRecord
        fields = ["id",
                  "real_name",
                  "amount",
                  "donation_date"]
