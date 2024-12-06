from django.urls import path, include
import reservation.views

urlpatterns = [
    path('', reservation.views.reservation),
    path('create', reservation.views.create),
    path('get_reservation_options', reservation.views.get_reservation_options, name='get_reservation_options'),

]