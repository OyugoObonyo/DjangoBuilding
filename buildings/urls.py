from django.urls import path
from . import views


urlpatterns = [
    path('add-building/', views.add_building, name="add-building"),
    path('update-building/<int:id>/', views.update_building, name="update-building"),
    path('delete-building/<int:id>/', views.delete_building, name="delete-building"),
    path('show-reviews/<int:id>/', views.show_reviews, name="show-reviews"),
    path('move-in-building/<int:id>/', views.move_in_building, name="move-in-building"),
    path('all-tenants/<int:id>/', views.view_tenants, name="view-tenants")
]