from django.conf.urls import re_path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls))
]
