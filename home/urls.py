from django.urls import path, include
import home.views

urlpatterns = [
    path('', home.views.home),
    path('test', home.views.test),

]