from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('education/', views.education, name="education"),
    path('projects/', views.projects, name="projects"),
    path('projects/<slug:slug>/', views.single_project, name="single_project"),
    path('achievements/', views.achievements, name="achievements"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
