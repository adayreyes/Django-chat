from django.contrib import admin
from .models import Message, Chat


class MessageAdmin(admin.ModelAdmin):
    list_display = ["text", "author", "created_at", "receiver"]
    fields = ["text", "author", "receiver", "chat"]
    search_fields = ["text"]


# Register your models here.

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
