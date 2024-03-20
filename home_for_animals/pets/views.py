from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from .models import Pet,Adoption,Project,Accounting,SelectedAnimals
from .serializers import PetSerializer,AdoptionSerializer,DonationSerializer,AccountingSerializer,ProjectSerializer
from rest_framework import generics,filters
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class PetListCreate(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'breed', 'position']


class PetDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDelete(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    success_url = reverse_lazy('pet_list')


@api_view(['POST'])
def submit_adoption_request(request, pet_id):
    user = request.user
    if not user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
    pet = Pet.objects.filter(id=pet_id).first()
    if not pet:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    adoption, created = Adoption.objects.get_or_create(user=user, pet=pet, defaults={'status': 'pending'})
    if not created:
        return Response({'message': 'Adoption request already submitted'}, status=status.HTTP_409_CONFLICT)

    serializer = AdoptionSerializer(adoption)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def view_adoption_status(request, pet_id):
    user = request.user
    if not user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        adoption = Adoption.objects.get(user=user, pet_id=pet_id)
        serializer = AdoptionSerializer(adoption)
        return Response(serializer.data)
    except Adoption.DoesNotExist:
        return Response({'error': 'Adoption request not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
# 已认证
def withdraw_adoption_request(request, pet_id):
    user = request.user
    # pet_id获取Pet对象
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        return Response({'error': 'Pet not found'}, status=status.HTTP_404_NOT_FOUND)
    try:
        adoption_request = Adoption.objects.get(user=user, pet=pet, status='pending')
    except Adoption.DoesNotExist:
        return Response({'error': 'Adoption request not found or already processed'}, status=status.HTTP_404_NOT_FOUND)

    adoption_request.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_adoption_request(request, adoption_id):
    user = request.user
    if not user.is_staff or not user.is_active: #？批准领养申请？
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    try:
        adoption = Adoption.objects.get(id=adoption_id)
    except Adoption.DoesNotExist:
        return Response({'error': 'Adoption request not found'}, status=status.HTTP_404_NOT_FOUND)

    if adoption.status != 'pending':
        return Response({'error': 'Adoption request is not pending'}, status=status.HTTP_400_BAD_REQUEST)
    adoption.status = 'approved'
    adoption.save()
    try:
        selected_animal = SelectedAnimals.objects.get(pet=adoption.pet)
        selected_animal.applications = F('applications') + 1
        selected_animal.save()
    except SelectedAnimals.DoesNotExist:
        pass
    return Response({'message': 'Adoption request approved'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def withdraw_adoption_request(request, adoption_id):
    user = request.user
    try:
        adoption = Adoption.objects.get(id=adoption_id, user=user, status='pending')
    except Adoption.DoesNotExist:
        return Response({'error': 'Adoption request not found or already processed'}, status=status.HTTP_404_NOT_FOUND)
    try:
        selected_animal = SelectedAnimals.objects.get(pet=adoption.pet)
        selected_animal.applications = F('applications') - 1
        selected_animal.save()
    except SelectedAnimals.DoesNotExist:
        pass
    adoption.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class DonationCreateView(APIView):
    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountingListView(APIView):
    def get(self, request):
        accountings = Accounting.objects.all()
        serializer = AccountingSerializer(accountings, many=True)
        return Response(serializer.data)
