from django.urls import path
from . import views


urlpatterns = [
    path('add-building/', views.add_building, name="add-building"),
    path('update-building/<int:id>/', views.update_building, name="update-building"),
    path('delete-building/<int:id>/', views.delete_building, name="delete-building"),
    path('review-building/<int:id>/', views.delete_building, name="review-building"),
    path('show-reviews/<int:id>/', views.delete_building, name="show-reviews")
]