from rest_framework import generics, permissions
from .models import AdoptionRequest
from .serializers import AdoptionRequestSerializer
from apps.users.models import User



class AdoptionRequestListCreateView(generics.ListCreateAPIView):
    """
    领养申请列表
    """
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # 认证

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # 是申请者


class AdoptionRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    申请详情
    """
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionRequestSerializer
    def get_object(self):
        obj = super().get_object()
        return obj
