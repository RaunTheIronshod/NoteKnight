# notes/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Note

class NotesViewTest(TestCase):

    def test_notes_homepage_empty(self):
        """
        If there are no notes, the page should display 'No notes yet.'
        """
        response = self.client.get(reverse('home'))  # Make sure 'home' matches your url name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Your Notes</h1>")
        self.assertContains(response, "No notes yet.")

    def test_notes_homepage_with_notes(self):
        """
        If notes exist, they should appear on the page.
        """
        note1 = Note.objects.create(title="Test Note 1", content="Content 1")
        note2 = Note.objects.create(title="Test Note 2", content="Content 2")

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, note1.title)
        self.assertContains(response, note2.title)
        self.assertNotContains(response, "No notes yet.")
