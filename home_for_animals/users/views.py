from pets.models import Adoption
from pets.serializers import AdoptionSerializer
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from django.shortcuts import render
# from django.views.decorators.http import require_http_methods
# from django.http import JsonResponse

from .models import DonationRecord, User, VolunteerRecord
from .serializers import VolunteerRecordSerializer, UserProfileSerializer,DonationRecordSerializer


class UserViewSet(
    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    视图集
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


    @action(detail=False, methods=["get"])
    def adoption_requests(self, request):
        """
        查看领养申请记录
        """
        user = request.user
        adoption_requests = Adoption.objects.filter(user=user)
        serializer = AdoptionSerializer(adoption_requests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def volunteer_records(self, request):
        """
        查看志愿记录
        """
        user = request.user
        records = VolunteerRecord.objects.filter(user=user)
        serializer = VolunteerRecordSerializer(records, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def donation_records(self, request):
        """
        查看捐赠记录
        """
        user = request.user
        records = DonationRecord.objects.filter(user=user)
        serializer = DonationRecordSerializer(records, many=True)
        return Response(serializer.data)

# from .models import ChatMessage, Feedback
# @require_http_methods(["GET"])
#
# def contact_view(request):
#     return render(request, '.html')
#
# @require_http_methods(["GET", "POST"])
# def feedback_view(request):
#     if request.method == 'GET':
#         return render(request, '.html')
#     elif request.method == 'POST':
#         feedback_text = request.POST.get('feedback')
#         # 输入框属性
#         if feedback_text:
#             feedback = Feedback(text=feedback_text)
#             feedback.save()
#             return JsonResponse({'status': 'success', 'message': '反馈成功!'})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Please provide feedback text.'}, status=400)
