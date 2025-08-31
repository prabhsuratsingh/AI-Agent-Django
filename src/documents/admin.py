from django.contrib import admin

from .models import Document

# Register your models here.
# admin.site.register(Document)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("owner","title", "active", "created_at")