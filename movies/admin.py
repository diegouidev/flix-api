from django.contrib import admin
from .models import Movies


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'genre')
    search_fields = ('title',)
    ordering = ('release_date',)
    list_filter = ('release_date', 'genre')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('genre')