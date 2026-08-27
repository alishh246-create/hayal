from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

# Customize admin site titles
admin.site.site_header = "HAYAL EVENTS Admin"
admin.site.site_title = "HAYAL EVENTS Portal"
admin.site.index_title = "Manage Contacts"
