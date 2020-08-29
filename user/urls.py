




from django.urls import path
from django.contrib.auth import views as  auth_views


#from . import views
from . import views 

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup),
    path('sign/',views.sign),
    path('home/' , views.home, name='home'),
    path('p/<slug:pk>/',views.profile, name='profile'),
   	path('p/<slug:pk>/<is_page>/update-profile/',views.updateprofile, name='updateprofile'),
    path('validate-username/', views.validate_username,name='validate-username'),

    path('createpage/', views.createpage.as_view(), name="createpage"),

    path('follow/<pk>/<is_page>/', views.follow, name='follow'),
    path('follows/<pk>/', views.follows, name='follows'),
    path('for_followers/', views.for_followers , name='for_followers'),

    path('ownlogin/', views.ownlogin, name='ownlogin'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/sign.html'), name='logout'),
   
   

    	





   
   


]