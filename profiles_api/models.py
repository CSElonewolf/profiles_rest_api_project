from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
	"""Manager for user profile"""

	def create_user(self, email,name,password=None):
		""" Create a new user profile"""
		if not email:
			raise ValueError('User must have an email address')
		email = self.normalize_email(email)
		user = self.model(
			email = email,
			name = name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,name,password):
		"""Create a superuser"""
		user = self.create_user(email,name,password)

		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
	"""Database model for users in the system"""
	email = models.EmailField(max_length = 255, unique = True)
	name = models.CharField(max_length = 255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default = False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Retrieve full name of user"""
		return self.name

	def get_short_name(self):
		"""Retrieve short name of user"""
		return self.name

	def __str__(self):
		"""Return a string representation of our user"""
		return self.email


class ProfileFeedItem(models.Model):
	""" Profile status update """
	user_profile = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete= models.CASCADE
	)
	status_text = models.CharField(max_length=255)
	craeted_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		"""Return the model as string """
		return self.status_text

