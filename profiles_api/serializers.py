from tkinter import E
from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
	"""serializers a user profile object"""

	class Meta:
		model = models.UserProfile
		fields =('id','name','email','password')
		extra_kwargs = {
			'password':{
				'write_only':True,
				'style':{
					'input_type':'password',
				}
			}
		}

		def create(self,valiadated_data):
			"""Create and return a new user"""
			user = models.User(
				name = valiadated_data['name'],
				email = valiadated_data['email'],
			)
			user.set_password(valiadated_data['password'])
			user.save()
			return user