from django.urls import path, include
from rest_framework import routers

from Mission.views import MissionViewSet, TargetViewSet

router = routers.DefaultRouter()
router.register("", MissionViewSet)
router.register("targets", TargetViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "Mission"
