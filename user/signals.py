
from django.db.models.signals import post_save
from . models import User,Page,Profile
from django.dispatch import receiver




''' Signal For Page  '''

''' Signal For User '''
@receiver(post_save,sender=Page)
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		#content_type=instance.content_type
		#object_id=instance.object_id
		Profile.objects.create(content_object=instance)



@receiver(post_save,sender=Page )
@receiver(post_save,sender=User )
def update_profile(sender,instance,created,**kwargs):
	if created == False:
		#print('instandce ;:',instance)
		if sender == User:
			p = Profile.objects.get(users__username=instance.username)
		else:
			p = Profile.objects.get(pages__name = instance.name)

		p.save()
		#instance.profile.save()
