from django.contrib import admin
from .models import Clone

@admin.register(Clone)
class CloneAdmin(admin.ModelAdmin):
    pass