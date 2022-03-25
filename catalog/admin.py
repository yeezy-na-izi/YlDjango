from django.contrib import admin
from catalog.models import Item
from catalog.models import Category, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'text')
    list_editable = ('is_published',)
    list_display_links = ('name', 'text')
    filter_horizontal = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_published', 'weight')
    list_editable = ('is_published',)
    list_display_links = ('slug',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('slug',)
