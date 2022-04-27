from django.urls import path
from . import views

urlpatterns = [
    path('all-buildings', views.get_all_buildings),
    path('get-building/<int:id>/', views.get_building)
]