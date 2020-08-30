from django.utils import timezone
from user.models import User
from django.utils.deprecation import MiddlewareMixin

class Lastlogin(MiddlewareMixin):
	def process_response(self, request, response):
		if request.user.is_authenticated:
			User.objects.filter(pk= request.user.pk).update(previous_login=timezone.now())
		return response