from django.urls import path, include
from team import views

urlpatterns = [
    path('create', views.create_team),
    path('<int:team_id>/edit_team/<str:op>/<int:user_id>', views.edit_team),
    path('<int:team_id>', views.team),





]