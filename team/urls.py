from django.urls import path, include
from team import views

urlpatterns = [
    path('create', views.create_team),
    path('<int:id>/edit_team/<str:op>', views.edit_team),
    path('<int:id>', views.team),





]