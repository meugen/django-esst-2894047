from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NodesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NodesDetailView.as_view(), name='notes.detail'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new')
]
