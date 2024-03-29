from . import views
from django.urls import path

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("video_feed/", views.video_feed, name="video_feed"),
    path("alert/", views.alert, name="alert"),
    path("inform/", views.inform, name="inform"),
    path("log/", views.log, name="log"),
]
