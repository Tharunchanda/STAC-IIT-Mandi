from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_view, name='CoreTeam'), 
    path('moreInfo', views.moreInfo, name='moreinfo'),
]
