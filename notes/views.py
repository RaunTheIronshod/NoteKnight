from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Note


# LIST ALL NOTES
class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    login_url = 'login'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


# VIEW NOTE DETAILS
class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    login_url = 'login'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


# CREATE NEW NOTE
class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Note created successfully!")
        return super().form_valid(form)


# UPDATE NOTE
class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Note updated!")
        return super().form_valid(form)

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


# DELETE NOTE
class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
    login_url = 'login'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Note deleted successfully!")
        return response


# REGISTER NEW USER
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Account created! You can now log in.")
        return super().form_valid(form)


# LOGIN VIEW WITH MESSAGE
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Logged in successfully.")
        return response


# LOGOUT VIEW WITH MESSAGE
class CustomLogoutView(LogoutView):
    next_page = 'login'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Logged out.")
        response = super().dispatch(request, *args, **kwargs)
        return response
