from django.urls import path
from . import views

urlpatterns = [
    path('home/<param>',views.home ,name='home'),
    path("contact", views.contact, name="contact"),
    path("info", views.apropos, name="apropos"),
]