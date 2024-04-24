from django.contrib import admin
from django.urls import path, include

from filmApp.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('izohlar', IzohlarModelViewSet)
router.register('kinolar', KinolarModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aktor/<int:pk>/', AktorlarAPIView.as_view()),

    path('hello/', HelloAPI.as_view()),
    path('aktyorlar/', AktyorlarAPI.as_view()),
    path('aktyorlar/<int:pk>/', AktyorAPI.as_view()),
    path('kinolar/', KinolarAPIView.as_view()),
    path('kinolar/<int:pk>/', KinoAPIView.as_view()),
    path('kinolar/<int:pk>/aktyorlar/', KinoAktyorlarAPIView.as_view()),
]
