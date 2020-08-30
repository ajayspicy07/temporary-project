

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Q

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib import messages
from .models import *
from .forms import *

from django.views.generic import CreateView,ListView,DetailView

from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request,'user/base.html')


def sign(request):
	if request.method=='POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user:home')
	else:
		form=UserRegistrationForm()
	return render(request,'user/sign.html',{'form':form})

def signup(request):
	if request.method=='POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user:login')
	else:
		form=UserRegistrationForm()
	return render(request,'user/signup.html',{'form':form})

def ownlogin(request):
	form = LoginForm()
	if request.method == 'POST':
		name = request.POST['username_email']
		password = request.POST['password']
		#password = 'pbkdf2_sha256$216000$g9NLoDQQD6Vs$Fk5KOgSCAeJ82N51xyTVIQtCdhtG9v8I5ezil9nXqo8='
		try :
			user = auth.authenticate(username=User.objects.get(email=name).username, password= password)
		except:
			user = auth.authenticate(username=name, password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('user:home')
		else:
			messages.error(request, 'Usernae or password is Wrong?')
		

	return render(request,'user/login.html', context={'form':form})


def profile(request,pk):
	profile=Profile.objects.get(slug=pk)
	if profile.content_object.is_page():
		members = profile.content_object.members.all()
		context = {'profile':profile,'members': members}
	else:
		context = {'profile':profile}

	return render(request,'user/profile.html', context)


class createpage(CreateView):
	model = Page
	fields = ['name']
	template_name = 'user/createpage.html'

	def form_valid(self, form):
		form.save()
		form.instance.members.add(self.request.user.user)
		#form.instance.college = self.request.user.user.college
		return super().form_valid(form)






def updateprofile(request,pk,is_page):
	profile = Profile.objects.get(slug=pk)
	if request.method == 'POST':
		profile_form =ProfileUpdateForm(request.POST ,request.FILES,
			instance=profile)
		if is_page=='True':
			print('page Update Post')
			unique_form = PageUpdateForm(request.POST,
				instance=Page.objects.get(name=profile.content_object))
		else:
			print('User update Post')
			#print(type(User.objects.get(username=profile.content_object.username)))
			unique_form = UserUpdateForm(request.POST,
				instance = User.objects.get(username=profile.content_object.username))
		
		 
		if profile_form.is_valid() and unique_form.is_valid():
			
			profile_form.save()
			unique_form.save()
			print('update view',profile.slug)
			return redirect('user:profile', pk=profile.slug)
		
	else:
		profile_form = ProfileUpdateForm(instance=profile)
		if is_page=='True':
			unique_form = PageUpdateForm(instance=Page.objects.get(name=profile.content_object))
		else:
			unique_form = UserUpdateForm(instance=User.objects.get(username=profile.content_object.username))

		#form= UserUpdateForm(instance=Profile.objects.get(slug=pk))
	
	context ={'profile_form':profile_form,'unique_form':unique_form}

	return render(request,'user/updateprofile.html',context)



def validate_username(request):
	username=request.GET.get('username',None)
	data = {
		'is_taken': User.objects.filter(username__iexact=username).exists()
	}
	
	if data['is_taken']:
		msg='User with that username already exists'
	elif ' ' in username :
		msg='Invalid Username'
	else:
		msg='Username is available'
		
	return JsonResponse(msg,safe=False)

@csrf_exempt
def follow(request,pk,is_page):
	print(pk)

	from_user=Profile.objects.filter(users__username=request.user).first()
	
	if is_page=='True':
		to_user= Profile.objects.filter(slug=pk).first()
	else:
		to_user =Profile.objects.filter(slug=pk).first() 
	
	#print(from_user,to_user,is_page)
	if Follower.objects.filter(from_profile=from_user,to_profile=to_user).exists():
		Follower.objects.filter(from_profile=from_user,to_profile=to_user).delete()
		#print('Deleted')
		msg = 'Deleted'

		
	else:
		Follower.objects.create(from_profile=from_user,to_profile=to_user)
		#print('Created')
		msg = 'Created'
	print(msg)
	return JsonResponse(msg,safe=False)


@csrf_exempt
def follows(request,pk):
	print(pk)
	#print('hello')
	to_user= Profile.objects.filter(slug=pk).first()
	
	from_user=Profile.objects.filter(users__username=request.user).first()
	print(from_user)
	if request.method == 'POST':
		if Follower.objects.filter(from_profile=from_user,to_profile=to_user).exists():
			Follower.objects.filter(from_profile=from_user,to_profile=to_user).delete()
			#print('Deleted')
			msg = 'Deleted'

		
		else:
			Follower.objects.create(from_profile=from_user,to_profile=to_user)
		#print('Created')
			msg = 'Created'
	print(msg)
	return JsonResponse(msg,safe=False)


	'''
	name = request.POST['user']
	#page = request.POST['page']
	from_user=Profile.objects.filter(id=int(name))
	to_user =Profile.objects.filter(id=int(page))
	print(from_user,to_user)
	if Follower.objects.filter(from_profile=from_user,to_profile=to_user).exists():
		Follower.objects.filter(from_profile=from_user,to_profile=to_user).delete()
		print('Deleted')
		msg = 'Follow'
	'''





def for_followers(request):
	#print('yes got it')
	pp = Profile.objects.get(users__username=request.user)
	#ff = list(Follower.objects.filter(from_profile=pp).values())
	fo = Follower.objects.filter(to_profile=pp)
	ff = list(pp.followers.all().values())
	print(request.user)
	print(pp)
	print(ff)
	profile_list=[]
	for i in range(len(ff)):
		profile = Profile.objects.get(id = ff[i]['to_profile_id'])
		profile_values =  {
						'name': str(profile), 
						'img': profile.img.url,
						'slug':profile.slug
		 				}
		profile_list.append(profile_values)
	print(profile_list)


	return JsonResponse(profile_list,safe=False)

		
		

	

	
	




