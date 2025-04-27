from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = ['id', 'title', 'content', 'slug', 'category', 'created_at', 'updated_at']

