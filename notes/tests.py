from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile, Note
from django.urls import reverse
from uuid import uuid4


class UserAndNoteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create users (signals auto-create UserProfiles)
        cls.user = User.objects.create_user(
            username=f'testuser_{uuid4()}',
            password='testpass123'
        )
        cls.user_profile = cls.user.userprofile
        cls.user_profile.role = 'user'
        cls.user_profile.save()

        cls.other_user = User.objects.create_user(
            username=f'otheruser_{uuid4()}',
            password='otherpass123'
        )
        cls.other_profile = cls.other_user.userprofile
        cls.other_profile.role = 'user'
        cls.other_profile.save()

        # Optional: create a note for the other user
        cls.other_note = Note.objects.create(
            user=cls.other_user,
            title='Other Note',
            content='Other content'
        )

    def setUp(self):
        self.client = Client()

    def test_user_registration(self):
        username = f'newuser_{uuid4()}'
        response = self.client.post(reverse('register'), {
            'username': username,
            'password1': 'newpass123',
            'password2': 'newpass123',
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username=username)
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_login(self):
        login_successful = self.client.login(username=self.user.username, password='testpass123')
        self.assertTrue(login_successful)

    def test_note_creation(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.post(reverse('note_create'), {
            'title': 'Test Note',
            'content': 'This is a test note content.'
        })
        self.assertEqual(response.status_code, 302)
        note = Note.objects.get(title='Test Note')
        self.assertEqual(note.user, self.user)

    def test_note_access_control(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.get(reverse('note_detail', args=[self.other_note.id]))
        self.assertEqual(response.status_code, 403)

    def test_admin_dashboard_access(self):
        self.client.login(username=self.user.username, password='testpass123')
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 403)

        self.user.is_staff = True
        self.user.save()
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
