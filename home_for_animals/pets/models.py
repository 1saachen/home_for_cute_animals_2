from django.db import models
from django.conf import settings
class Pet(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='pets_avatars/', null=True, blank=True)
    breed = models.CharField(max_length=100)
    distribution = models.TextField()
    weight = models.FloatField()
    health_status = models.CharField(max_length=100)
    is_adoptable = models.BooleanField(default=True)



class Adoption(models.Model):
    pet = models.ForeignKey(Pet, related_name='adoptions', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='adoptions', on_delete=models.CASCADE)
    adopted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=100)

class Accounting(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    donation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('pet', 'user','donation', 'donation_date')