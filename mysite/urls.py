"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf.urls.static import static
from django.contrib.auth import views as  auth_views

from django.conf import settings
import user,post,project


urlpatterns = [
    path('admin/', admin.site.urls),
    
    url('ckeditor/', include('ckeditor_uploader.urls')),
    path('tinymce/', include('tinymce.urls')),
  
   
    path('',include('user.urls')),
   	path('',include('post.urls')),
   	path('',include('project.urls')),

     path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='templates/password-reset.html'),
         name='password-reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='templates/password-reset-done.html'),
         name='password-reset-done'),

    path('password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='templates/password_reset_confirm.html'),
         name='password_reset_confirm'),
   
   

   
   

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
