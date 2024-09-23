from django.urls import path, include
import team.views

urlpatterns = [
    path('', team.views.team),

]