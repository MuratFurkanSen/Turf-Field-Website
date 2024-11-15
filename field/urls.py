from django.urls import path, include
import field.views
urlpatterns = [
    path('', field.views.fields),
    path('create', field.views.createField, name='creation'),
]

