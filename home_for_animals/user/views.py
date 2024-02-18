from rest_framework import viewsets, mixins, status,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, VolunteerRecord, DonationRecord
from .serializers import UserSerializer, VolunteerRecordSerializer, DonationRecordSerializer
from apps.adoptions.models import AdoptionRequest
from apps.adoptions.serializers import AdoptionSerializer

class UserViewSet(mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    视图集
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'
    # 查看方式

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance == request.user:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        # else:  查看失败

    def update(self, request, *args, **kwargs):
        """
        用户更新信息
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance == request.user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)  # 失败

    @action(detail=False, methods=['get'])
    def adoption_requests(self, request):
        """
        查看领养申请记录
        """
        user = request.user
        adoption_requests = AdoptionRequest.objects.filter(user=user)
        serializer = AdoptionSerializer(adoption_requests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def volunteer_records(self, request):
        """
        查看志愿记录
        """
        user = request.user
        records = VolunteerRecord.objects.filter(user=user)
        serializer = VolunteerRecordSerializer(records, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def donation_records(self, request):
        """
        查看捐赠记录
        """
        user = request.user
        records = DonationRecord.objects.filter(user=user)
        serializer = DonationRecordSerializer(records, many=True)
        return Response(serializer.data)


