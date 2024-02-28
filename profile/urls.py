from django.urls import path
from profile.views import profile
from App_marketplace.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('profile/', profile, name='profile'),
]
