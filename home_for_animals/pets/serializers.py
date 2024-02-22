from rest_framework import serializers
from .models import Pet,Adoption,Donation,Accounting,Project

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'  # 或者列出所有具体字段

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ['id', 'pet', 'user', 'adopted_at','request_date', 'status']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'target_amount']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'project', 'amount', 'donor_name']
class AccountingSerializer(serializers.ModelSerializer):
    donation = DonationSerializer()

    class Meta:
        model = Accounting
        fields = ['id', 'donation', 'donation_date']