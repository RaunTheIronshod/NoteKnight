from django.urls import path
from . import views

urlpatterns = [
    # List all notes (homepage)
    path('', views.NoteList.as_view(), name='note_list'),

    # Create a new note
    path('create/', views.NoteCreate.as_view(), name='note_create'),

    # View a single note
    path('<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),

    # Update a note
    path('<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),

    # Delete a note
    path('<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),
]
