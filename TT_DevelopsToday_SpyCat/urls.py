from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/spycats/", include("SpyCat.urls", namespace="SpyCat")),
]
