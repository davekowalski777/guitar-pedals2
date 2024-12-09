from django.contrib import admin
from .models import Manufacturer, PedalType, Pedal, Comment, Author

# Register your models here.

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

@admin.register(PedalType)
class PedalTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Pedal)
class PedalAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'pedal_type', 'price', 'is_discontinued')
    list_filter = ('manufacturer', 'pedal_type', 'is_discontinued')
    search_fields = ('name', 'manufacturer__name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'pedal', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('author_name', 'email', 'content', 'pedal__name')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"
