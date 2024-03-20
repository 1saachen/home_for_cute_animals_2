from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
# from .views import contact_view, feedback_view

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('user/', include(router.urls)),

    path('user/adoption/',
         UserViewSet.as_view({'get': 'adoption_requests'}),
         name='adoption'),

    path('user/volunteer/',
         UserViewSet.as_view({'get': 'volunteer_records'}),
         name='volunteer_records'),

    path('user/donation/',
         UserViewSet.as_view({'get': 'donation_records'}),
         name='donation_records'),

    # path('contact/', contact_view.as_view(), name='contact'),
    # path('feedback/', feedback_view.as_view(), name='feedback'),
]
