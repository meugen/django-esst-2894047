from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'

class NodesListView(ListView):
    model = Notes
    context_object_name = 'notes'

class NodesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
