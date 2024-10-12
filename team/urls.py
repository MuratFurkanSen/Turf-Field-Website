from django.urls import path, include
from team import views

urlpatterns = [
    path('create', views.create_team),
    path('<int:id>/update', views.edit_team),
    path('<int:id>', views.team),





]