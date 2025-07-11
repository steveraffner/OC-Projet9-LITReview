from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.TextField(
        max_length=2048, blank=True, verbose_name="Description"
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
    )
    image = models.ImageField(
        null=True, blank=True, upload_to="tickets/", verbose_name="Image"
    )
    time_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Billet"
        verbose_name_plural = "Billets"
        ordering = ["-time_created"]


class Review(models.Model):
    ticket = models.ForeignKey(
        to=Ticket, on_delete=models.CASCADE, verbose_name="Billet"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Note"
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
    )
    headline = models.CharField(max_length=128, verbose_name="Titre")
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    time_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création"
    )

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = "Critique"
        verbose_name_plural = "Critiques"
        ordering = ["-time_created"]


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Utilisateur",
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
        verbose_name="Utilisateur suivi",
    )

    def __str__(self):
        return f"{self.user.username} suit {self.followed_user.username}"

    class Meta:
        unique_together = ("user", "followed_user")
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"
