from django.contrib import admin
from .models import Ticket, Review, UserFollows


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "time_created")
    list_filter = ("time_created", "user")
    search_fields = ("title", "description")
    readonly_fields = ("time_created",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("headline", "ticket", "user", "rating", "time_created")
    list_filter = ("rating", "time_created", "user")
    search_fields = ("headline", "body", "ticket__title")
    readonly_fields = ("time_created",)


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("user", "followed_user")
    list_filter = ("user", "followed_user")
    search_fields = ("user__username", "followed_user__username")
