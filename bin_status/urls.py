from rest_framework.routers import DefaultRouter
from .views import BinStatusViewSet, latest_bin_status 
from django.urls import path, include

router = DefaultRouter()
router.register(r'bin-status', BinStatusViewSet, basename='bin-status')

urlpatterns = [
    path('', include(router.urls)),
    path('bin-status/latest/', latest_bin_status), 
]
