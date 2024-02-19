from django.urls import path
from . import views

urlpatterns = [
    path('pets/<int:pet_id>/',
         views.pet_detail,
         name='pet_detail'),
    path('user/<int:pet_id>/withdraw/',
         views.withdraw_adoption_request,
         name='withdraw_adoption_request'),
]