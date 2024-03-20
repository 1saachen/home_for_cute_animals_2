from django.db import models
from django.conf import settings
from django.utils import timezone
class Pet(models.Model):
    name = models.CharField(max_length=100)
    DISTRIBUTION_CHOICE = [
        ('W', '文理学部'),
        ('G', '工学部'),
        ('X', '信息学部'),
        ('Y', '医学部'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    CONDITION_CHOICES =[
        ('X','在校'),
        ('L','被领养'),
        ('M','喵星'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='Unknown')
    breed = models.CharField(max_length=100)
    status = models.CharField(max_length=20,blank=True,null=True)
    condition = models.CharField(max_length=1,choices=CONDITION_CHOICES,default='Unknown')
    position = models.CharField(max_length=100, choices=DISTRIBUTION_CHOICE, default='Unknown')
    feature = models.CharField(max_length=20, blank=True, null=True)
    range = models.CharField(max_length=100, blank=True, null=True)
    personality = models.CharField(max_length=100, blank=True, null=True)
    sterilization = models.BooleanField(default=False)
    health = models.CharField(max_length=100)
    social = models.CharField(max_length=100,blank=True,null=True)
    other = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='pets_avatars/', null=True, blank=True)


class SelectedAnimals(models.Model):
    """
    待领养宠物信息
    """
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='selected_animals')
    date = models.DateField()
    status = models.CharField(max_length=20, blank=True, null=True)
    applications = models.IntegerField(default=0)  #
    #申请人数
    requirements = models.TextField()

    def __str__(self):
        return f"{self.pet.name} "

class Adoption(models.Model):
    pet = models.ForeignKey(Pet, related_name='adoptions', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='adoptions', on_delete=models.CASCADE)
    adopted_at = models.DateTimeField(auto_now_add=True)
    request_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    class Meta:
        unique_together = ('pet', 'user')

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
       unique_together = (('donation', 'donation_date'),)