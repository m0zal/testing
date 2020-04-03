from rest_framework import routers
from api_testing import test_api_views

router = routers.DefaultRouter()
router.register(r"test", test_api_views.TestViewSet)
