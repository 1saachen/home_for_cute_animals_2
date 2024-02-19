from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from pets.models import Pet
from .models import AdoptionRequest
from django.urls import reverse

@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    user = request.user
    try:
        adoption_request = AdoptionRequest.objects.get(user=user, pet=pet)
    except AdoptionRequest.DoesNotExist:
        adoption_request = None

    context = {
        'pet': pet,
        'adoption_request': adoption_request,
    }
    return render(request, 'adoptions/pet_detail.html', context)

@login_required
def withdraw_adoption_request(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    user = request.user
    return redirect(reverse('pet_detail', args=[pet_id]))