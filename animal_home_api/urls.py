from django.urls import path , include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'pet', views.PetViewSet)
router.register(r'petphoto', views.PetPhotoViewSet)
router.register(r'interested', views.InterestedViewSet)
router.register(r'message', views.MessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]