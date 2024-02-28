from django.urls import path
from . import views
from App_marketplace.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('wineries/', views.winery_list, name='winery_list'),
    path('admin/approve/<int:winery_id>/', views.approve_winery, name='approve_winery'),
    path('add_winery/', views.add_winery, name='add_winery'),
    path('winery/<int:winery_id>/', views.winery_detail, name='winery_detail'),
]
