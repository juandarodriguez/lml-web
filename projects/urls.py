from django.urls import path
from . import views

from .views import UserHome, ProjectView

urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
    path('home', UserHome.as_view(), name='user_home'),
    path('api/hello2', views.Hello2View.as_view(), name='hello2'),
    path('api/project', views.ApiProjectListView.as_view(), name='projects'),
    path('api/project/<int:pk>', views.ApiProjectDetailView.as_view())
]