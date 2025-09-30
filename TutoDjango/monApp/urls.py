from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path("home/<param>",views.accueil ,name='accueil'),
    path("contact/", views.ContactView, name="contact"),
    path("info/", views.AboutView.as_view(), name="apropos"),
    path("produit/",views.ProduitCreateView.as_view(), name="crt_prdt"),
    path("produits/", views.ProduitListView.as_view(),name="lst_prdts"),
    path("produit/<pk>/",views.ProduitDetailView.as_view(), name="dtl_prdt"),
    path("categories/", views.CategorieListView.as_view(), name="lst_cats"),
    path("categories/<pk>/", views.CategorieDetailView.as_view(), name="dtl_cat"),
    path("statuts/", views.StatutListView.as_view(), name="lst_stats"),
    path("statuts/<pk>/", views.StatutDetailView.as_view(), name="dtl_statut"),
    path("rayons/", views.RayonListView.as_view(), name="lst_rays"),
    path("rayons/<pk>/", views.RayonDetailView.as_view(), name="dtl_ray"),
    path("home/", views.HomeView.as_view(),name="home"),
    path("home/<param>", views.HomeView.as_view()),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    path('envoi_mail/', views.sentEmailView.as_view(), name='email_sent'),
]