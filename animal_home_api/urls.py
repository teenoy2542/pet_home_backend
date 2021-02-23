from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from knox import views as knox_views

from animal_home_api.views import PetView, PetDetailView, UserDetailView, RegisterAPI, LoginAPI


urlpatterns = [
    path('api/user/register', RegisterAPI.as_view(), name='register'),
    path('api/user/<int:id>', UserDetailView.as_view()),
    path('api/pet', PetView.as_view()),
    path('api/pet/<int:pet_id>', PetDetailView.as_view()),
    path('api/user/login', LoginAPI.as_view(), name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)