from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Notes

class NodesListView(ListView):
    model = Notes
    context_object_name = 'notes'

class NodesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
