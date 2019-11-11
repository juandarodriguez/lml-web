from django.urls import path
from . import views

from .views import UserHome

urlpatterns = [
    path('', UserHome.as_view(), name='user_home'),
    path('api/hello2', views.Hello2View.as_view(), name='hello2'),
]