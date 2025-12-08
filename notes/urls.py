from django.urls import path
from .views import NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete

urlpatterns = [
    path('', NoteList.as_view(), name='note_list'),               # /note/
    path('create/', NoteCreate.as_view(), name='note_create'),    # /note/create/
    path('<int:pk>/', NoteDetail.as_view(), name='note_detail'),  # /note/1/
    path('<int:pk>/edit/', NoteUpdate.as_view(), name='note_edit'),   # /note/1/edit/
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note_delete'), # /note/1/delete/
]
