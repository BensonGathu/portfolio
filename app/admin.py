from django.contrib import admin
from .models import Languages,Profile,Project
# Register your models here.
admin.site.register(Languages)
admin.site.register(Project)
admin.site.register(Profile)