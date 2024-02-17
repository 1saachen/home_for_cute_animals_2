from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pet,Adoption
from .serializers import PetSerializer,AdoptionSerializer
from rest_framework import generics
from django.urls import reverse_lazy
from rest_framework.decorators import api_view

class PetListCreate(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDelete(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    success_url = reverse_lazy('pet_list')  # 注意：在 DRF 中通常不直接使用 `success_url`


@api_view(['POST'])
def submit_adoption_request(request, pet_id):
    user = request.user
    if not user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    pet = Pet.objects.filter(id=pet_id).first()
    if not pet:
        return Response({'error': 'Pet not found'}, status=status.HTTP_404_NOT_FOUND)

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
