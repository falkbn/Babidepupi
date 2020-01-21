from django.contrib import admin
from main.models import User, Rating, Peripheral

admin.site.register(Peripheral)
admin.site.register(User)
admin.site.register(Rating)
