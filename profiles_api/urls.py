from xml.etree.ElementInclude import include
from django.urls import path,include
from rest_framework.routers import DefaultRouter

# inner project import
from . import views

# create a router and register our viewset with it
router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
	path('',include(router.urls))
]