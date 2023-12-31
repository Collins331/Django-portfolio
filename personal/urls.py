from django.urls import path
from . import views

app_name = "personal"
urlpatterns = [
    path("", views.home, name="home"),
    path("", views.portfolio, name="portfolio"),
    path("resume", views.resume, name="resume"),
    path("form", views.form, name="form"),
    path("viewdata", views.viewdata, name="view-data")
 ]