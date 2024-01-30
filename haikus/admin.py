from django.contrib import admin
from .models import Haiku, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Haiku)
class HaikuAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'tag')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('create_date', 'tag')

    class Meta:
        model = Haiku
        fields = ('content',)

