from django.urls import path
from .views import NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete

urlpatterns = [
    path('', NoteList.as_view(), name='note_list'),
    path('<int:pk>/', NoteDetail.as_view(), name='note_detail'),
    path('create/', NoteCreate.as_view(), name='note_create'),
    path('<int:pk>/update/', NoteUpdate.as_view(), name='note_update'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note_delete'),
]
