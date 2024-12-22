from django.urls import path
import facility.views
urlpatterns = [
    path('create', facility.views.facility, name='facility'),
]