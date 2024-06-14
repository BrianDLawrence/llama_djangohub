from django.contrib import admin
from .models import Actions, Context

class ActionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Actions, ActionsAdmin)
admin.site.register(Context, ActionsAdmin)
