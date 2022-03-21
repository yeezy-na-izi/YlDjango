from django.contrib import admin
from catalog.models import Item
from catalog.models import Category, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'text')
    list_editable = ('is_published',)
    list_display_links = ('name', 'text')


admin.site.register(Category)
admin.site.register(Tag)
