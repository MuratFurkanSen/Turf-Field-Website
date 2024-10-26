from django.urls import path, include
import field.views

urlpatterns = [
    path('create', field.views.createField, name='creation'),

]