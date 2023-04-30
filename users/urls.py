from django.conf.urls import include
import django.conf.urls
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from users.views import *

router = DefaultRouter()

urlpatterns = [
    re_path('api/', include(router.urls)),
]

