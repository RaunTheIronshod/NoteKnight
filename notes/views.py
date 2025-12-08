from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Note


# LIST ALL NOTES
class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    login_url = 'login'

    def get_queryset(self):
        # Only show notes belonging to the logged-in user
        return Note.objects.filter(user=self.request.user)


# VIEW NOTE DETAILS
class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    login_url = 'login'

    def get_queryset(self):
        # Only allow user to view their own notes
        return Note.objects.filter(user=self.request.user)


# CREATE NEW NOTE
class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note_list')
    login_url = 'login'

    def form_valid(self, form):
        # Assign the logged-in user before saving
        form.instance.user = self.request.user
        return super().form_valid(form)


# UPDATE NOTE
class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note_list')
    login_url = 'login'

    def get_queryset(self):
        # Only allow user to edit their own notes
        return Note.objects.filter(user=self.request.user)


# DELETE NOTE
class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
    login_url = 'login'

    def get_queryset(self):
        # Only allow user to delete their own notes
        return Note.objects.filter(user=self.request.user)


# REGISTER NEW USER
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
