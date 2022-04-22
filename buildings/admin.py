from django.contrib import admin
from .models import Building, Review, Tag


admin.site.register(Building)
admin.site.register(Review)
admin.site.register(Tag)