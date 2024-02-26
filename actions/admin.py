from django.contrib import admin
from .models import Actions

class ActionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Actions, ActionsAdmin)
