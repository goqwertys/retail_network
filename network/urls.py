from rest_framework.routers import SimpleRouter

from network.apps import NetworkConfig
from network.views import NetworkViewSet, ProductViewSet

app_name = NetworkConfig.name

router = SimpleRouter()
router.register('nodes', NetworkViewSet)
router.register('products', ProductViewSet)

urlpatterns = []

urlpatterns += router.urls
