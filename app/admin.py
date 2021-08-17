from django.contrib import admin
from .models import Languages,Profile,Project
# Register your models here.

class ProjectLanguages(admin.ModelAdmin):
    filter_horizontal=('languages',)

admin.site.register(Languages)
admin.site.register(Project,ProjectLanguages)
admin.site.register(Profile)
