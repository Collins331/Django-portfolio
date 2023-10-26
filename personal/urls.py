from django.urls import path
from . import views

app_name = "personal"
urlpatterns = [
    path("", views.home, name="home"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("resume", views.resume, name="resume")
]