from django.urls import path
from . import views

from . import views
urlpatterns = [
    path('rooms/', views.RoomApiView.as_view()),
    path('players/', views.PlayerApiView.as_view())
]
