from re import search
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

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
