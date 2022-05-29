from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import NotificationViewSet, NotificationOperationViewSet, ReasonOptionViewSet, SystemConfigViewSet, \
    ZipcodeViewSet, TaxViewSet

app_name = "src.system_management"

router = DefaultRouter()
router.register(r'taxes', TaxViewSet)
router.register(r'zipcodes', ZipcodeViewSet)
router.register(r'reasons', ReasonOptionViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'notification-operations', NotificationOperationViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
