from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('clipboards', views.ClipboardViewSet, basename='clipboards')

clipboard_router = routers.NestedDefaultRouter(router, 'clipboards', lookup='clipboard')
clipboard_router.register('items', views.ClipboardItemViewSet, basename='clipboard-items')

urlpatterns = router.urls + clipboard_router.urls
