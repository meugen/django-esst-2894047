from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NodesListView.as_view()),
    path('notes/<int:pk>', views.NodesDetailView.as_view()),
]
