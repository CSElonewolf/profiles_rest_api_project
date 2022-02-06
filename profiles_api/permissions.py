from rest_framework import permissions



class UpdateOwnPermissions(permissions.BasePermission):
	"""Allow user t edit thier own profile """

	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		# if the authenticated user is not same as the user editing
		return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
	"""Allow users to update their own status"""

	def has_object_permission(self,request,view,obj):
		"""Check the user is trying to update their own status """
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.user_profile.id == request.user.id 