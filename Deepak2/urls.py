from . import views
from django.urls import path

urlpatterns = [
    path("home",views.home),
    path("about",views.about),
    path("gallery",views.gallery),
    path("contact",views.contact),
    path("help",views.help),
]
