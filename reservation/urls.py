from django.urls import path, include
import reservation.views

urlpatterns = [
    path('', reservation.views.reservation),
    path('create', reservation.views.create),
    path('get_date_options', reservation.views.get_date_options, name='get_date_options'),

]