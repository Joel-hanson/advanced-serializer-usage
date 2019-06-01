from rest_framework.routers import DefaultRouter
from .views import BookModelViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'book', BookModelViewSet, base_name='book')


urlpatterns = router.urls

