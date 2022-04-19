from django.urls import path
from . import views


urlpatterns = [
    path('add-building', views.add_building, name="add-building")
]