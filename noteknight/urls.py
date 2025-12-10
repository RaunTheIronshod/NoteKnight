from django.contrib import admin
from django.urls import path, include
from notes import views as note_views
from .views import admin_dashboard

urlpatterns = [
    # --- Admin ---
    path('admin/', admin.site.urls),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    # --- Auth ---
    path('login/', note_views.CustomLoginView.as_view(), name='login'),
    path('logout/', note_views.CustomLogoutView.as_view(), name='logout'),
    path('register/', note_views.RegisterView.as_view(), name='register'),

    # --- Notes ---
    path('', include('notes.urls')),          # main homepage = notes list
    path('note/', include('notes.urls')),     # optional secondary path
]

