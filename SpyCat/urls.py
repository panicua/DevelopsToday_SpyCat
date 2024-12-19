from django.urls import path, include
from rest_framework import routers
from SpyCat.views import SpyCatViewSet

router = routers.DefaultRouter()
router.register("", SpyCatViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "SpyCat"
