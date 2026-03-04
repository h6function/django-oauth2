"""
URL configuration for idp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from auth import views as auth_views
from idp_resource import views as resource_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/authorize/', auth_views.authorize, name='authorize'),
    path('oauth/token/', auth_views.issue_token, name='issue_token'),
    path('user/email/', resource_views.user_email, name='user_email'),
    path('user/name/', resource_views.user_name, name='user_name'),
]
