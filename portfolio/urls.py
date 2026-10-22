from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_views, name='home'),
    path('projects/',views.projects_views, name='projects'),
    path('skills/',views.skills_views, name='skills'),
]