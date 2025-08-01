from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('birthday',)
