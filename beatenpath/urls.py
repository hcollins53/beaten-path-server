"""
URL configuration for beatenpath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from pathsapi.views import login_user, register_user, TrailView, UserView, CampingSiteView, WantListView, CompletedListView, ReviewView, UserProfileListView, MessageView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'trails', TrailView, 'trail')
router.register(r'campingsites', CampingSiteView, 'campingsite')
router.register(r'wantlists', WantListView, 'wantlist')
router.register(r'completedlists', CompletedListView, 'completedlist')
router.register(r'reviews', ReviewView, 'review')
router.register(r'userprofiles', UserProfileListView, 'userprofile')
router.register(r'messages', MessageView, 'message')
router.register(r'users', UserView, 'user')
urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
