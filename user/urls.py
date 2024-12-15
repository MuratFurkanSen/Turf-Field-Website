from django.urls import path, include
from user import views

urlpatterns = [
    path('register',views.user_register, name='user_register' ),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('invites', views.user_invites, name='user_invites'),
    path('add_friend/<int:invite_id>', views.accept_friend_invite, name='user_add_friend'),
    path('add_team/<int:invite_id>', views.accept_team_invite, name='user_add_team'),
    path('decline_friend/<int:invite_id>', views.decline_friend_invite, name='user_decline_friend'),
    path('decline_team/<int:invite_id>', views.decline_team_invite, name='user_decline_team'),

]