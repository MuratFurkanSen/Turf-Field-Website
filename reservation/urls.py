from django.urls import path, include
import reservation.views

urlpatterns = [
    path('', reservation.views.reservation),

]