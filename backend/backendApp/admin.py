from django.contrib import admin
from backendApp.models import PlayerClass

class PlayerClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'wins')

admin.site.register(PlayerClass, PlayerClassAdmin)