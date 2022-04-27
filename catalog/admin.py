from django.contrib import admin

from catalog.models import Category, Item, Tag, Image


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'text', 'image_tmb')
    list_editable = ('is_published',)
    list_display_links = ('name', 'text')
    filter_horizontal = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_published', 'weight')
    list_editable = ('is_published',)
    list_display_links = ('name', 'slug',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name', 'slug',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'item')
