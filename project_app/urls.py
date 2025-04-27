from django.urls import path
from .views import *

urlpatterns = [
  path('notes/', notes, name='notes'),
  path('note/<slug:slug>/', note_details, name='note_details'),
  path('search-note/', search_notes, name='search_notes'),
]