from django.contrib import admin
from .models import *

class NoteAdmin(admin.ModelAdmin):
  list_display = ('title', 'category', 'created_at', 'updated_at')
  # search_fields = ('title', 'content')
  # list_filter = ('created_at', 'updated_at')
  # ordering = ('-created_at',)

admin.site.register(Note, NoteAdmin)