from re import search
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers
from . import models
from . import permissions
# Create your views here.



class UserProfileViewSet(viewsets.ModelViewSet):
	""" Handle creating and updatng profiles """
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	# add permission
	permission_classes = [permissions.UpdateOwnPermissions,]
	# add authentication
	authentication_classes = [TokenAuthentication]
	# allows search
	filter_backends = [filters.SearchFilter]
	search_fields = ['name','email']


class UserLoginAPIView(ObtainAuthToken):
	""" handle creating user authentication token """
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
	"""Handles creating,raeding and updaing profile feed items """
	serializer_class = serializers.ProfileFeedItemSerializer
	queryset = models.ProfileFeedItem.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnStatus, IsAuthenticatedOrReadOnly)


	def perform_create(self,serializer):
		""""Sets the user profile to the logged in user"""
		serializer.save(user_profile = self.request.user)

