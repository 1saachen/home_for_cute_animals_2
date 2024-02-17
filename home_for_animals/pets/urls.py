from django.urls import path
from .views import PetListCreate, PetDetailUpdate, PetDelete
from .views import submit_adoption_request, view_adoption_status
from .views import ProjectListView, DonationCreateView, AccountingListView

urlpatterns = [
    path('pets/', PetListCreate.as_view(), name='pet_list_create'),
    path('pets/<int:pk>/', PetDetailUpdate.as_view(), name='pet_detail_update'),
    path('pets/<int:pk>/delete/', PetDelete.as_view(), name='pet_delete'),
    path('adopt/<int:pet_id>/', submit_adoption_request, name='submit_adoption_request'),
    path('adoption-status/<int:pet_id>/', view_adoption_status, name='view_adoption_status'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('donate/', DonationCreateView.as_view(), name='donate'),
    path('accounting/', AccountingListView.as_view(), name='accounting'),
]
