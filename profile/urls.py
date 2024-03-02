from django.urls import path
from .views import profile_redirect
from profile.views import profile
from App_marketplace.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('profile/', profile_redirect, name='profile_redirect'),
    path('user/profile/', profile, name='profile'),
]
