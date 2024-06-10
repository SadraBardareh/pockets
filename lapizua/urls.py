from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('lapizua', views.LapizuaPocketViewSet, basename='lapizua')

urlpatterns = router.urls