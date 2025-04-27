from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

class Note(models.Model):
  CATEGORY =  (
    ('BUSINESS', 'Business'),
    ('PERSONAL', 'Personal'),
    ('IMPORTANT', 'Important'),
  )
  title = models.CharField(max_length=100)
  content = models.TextField()
  slug = models.SlugField(unique=True, blank=True, null=True)
  category = models.CharField(max_length=50, choices=CATEGORY, default='PERSONAL')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title
  
  def save(self, *args, **kwargs):
    if not self.slug:
      # Generate initial slug
      slug_base = slugify(self.title)
      slug = slug_base
      # Check if the slug is unique and update if necessary
      if Note.objects.filter(slug=slug).exists():
        slug = f"{slug_base}-{get_random_string(5)}"
      self.slug = slug
    super(Note, self).save(*args, **kwargs)