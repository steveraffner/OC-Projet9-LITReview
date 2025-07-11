from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentification
    path("signup/", views.signup, name="signup"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", views.user_logout, name="logout"),
    # Flux principal
    path("", views.feed, name="feed"),
    # Billets (Tickets)
    path("ticket/create/", views.ticket_create, name="ticket_create"),
    path("ticket/<int:ticket_id>/update/", views.ticket_update, name="ticket_update"),
    path("ticket/<int:ticket_id>/delete/", views.ticket_delete, name="ticket_delete"),
    # Critiques (Reviews)
    path("review/create/<int:ticket_id>/", views.review_create, name="review_create"),
    path(
        "review/create-with-ticket/",
        views.review_create_with_ticket,
        name="review_create_with_ticket",
    ),
    path("review/<int:review_id>/update/", views.review_update, name="review_update"),
    path("review/<int:review_id>/delete/", views.review_delete, name="review_delete"),
    # Abonnements
    path("follow/", views.follow_list, name="follow_list"),
    path("follow/create/", views.follow_create, name="follow_create"),
    path("follow/<int:follow_id>/delete/", views.follow_delete, name="follow_delete"),
    # Posts de l'utilisateur
    path("my-posts/", views.user_posts, name="user_posts"),
]
