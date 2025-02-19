from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserProfileViewSet, UserCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register('profiles', UserProfileViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny, )), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny, )), name='refresh'),
]

urlpatterns += router.urls
