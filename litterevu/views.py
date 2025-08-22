from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import CharField, Value, Q
from django.core.paginator import Paginator
from .models import Ticket, Review, UserFollows
from .forms import SignUpForm, TicketForm, ReviewForm, TicketReviewForm, UserFollowsForm


def signup(request):
    """Vue d'inscription"""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec succès!")
            return redirect("feed")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def user_logout(request):
    """Vue de déconnexion"""
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect("login")


@login_required
def feed(request):
    """Vue du flux principal"""
    # Récupérer les billets des utilisateurs suivis et de l'utilisateur connecté
    followed_users = request.user.following.values_list("followed_user", flat=True)

    tickets = Ticket.objects.filter(
        Q(user__in=followed_users) | Q(user=request.user)
    ).annotate(content_type=Value("TICKET", CharField()))

    # Récupérer les critiques des utilisateurs suivis et de l'utilisateur connecté
    reviews = Review.objects.filter(
        Q(user__in=followed_users) | Q(user=request.user)
    ).annotate(content_type=Value("REVIEW", CharField()))

    # Ajouter les critiques en réponse aux billets de l'utilisateur connecté
    # mais seulement celles qui ne sont pas déjà incluses dans les critiques ci-dessus
    own_tickets = Ticket.objects.filter(user=request.user)
    reviews_on_own_tickets = (
        Review.objects.filter(ticket__in=own_tickets)
        .exclude(user=request.user)
        .exclude(user__in=followed_users)
        .annotate(content_type=Value("REVIEW", CharField()))
    )

    # Combiner tous les posts
    all_posts = sorted(
        chain(tickets, reviews, reviews_on_own_tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )

    # Pagination
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request, "feed.html", {"posts": posts})


@login_required
def ticket_create(request):
    """Vue de création d'un billet"""
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, "Votre billet a été créé avec succès!")
            return redirect("feed")
    else:
        form = TicketForm()
    return render(request, "ticket_create.html", {"form": form})


@login_required
def ticket_update(request, ticket_id):
    """Vue de modification d'un billet"""
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre billet a été modifié avec succès!")
            return redirect("feed")
    else:
        form = TicketForm(instance=ticket)
    return render(request, "ticket_update.html", {"form": form, "ticket": ticket})


@login_required
def ticket_delete(request, ticket_id):
    """Vue de suppression d'un billet"""
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == "POST":
        ticket.delete()
        messages.success(request, "Votre billet a été supprimé avec succès!")
        return redirect("feed")
    return render(request, "ticket_confirm_delete.html", {"ticket": ticket})


@login_required
def review_create(request, ticket_id):
    """Vue de création d'une critique en réponse à un billet"""
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Vérifier si l'utilisateur a déjà critiqué ce billet
    if Review.objects.filter(ticket=ticket, user=request.user).exists():
        messages.error(request, "Vous avez déjà critiqué ce billet.")
        return redirect("feed")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            messages.success(request, "Votre critique a été créée avec succès!")
            return redirect("feed")
    else:
        form = ReviewForm()
    return render(request, "review_create.html", {"form": form, "ticket": ticket})


@login_required
def review_create_with_ticket(request):
    """Vue de création d'une critique avec un nouveau billet"""
    if request.method == "POST":
        form = TicketReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # Créer le billet
            ticket = Ticket.objects.create(
                title=form.cleaned_data["ticket_title"],
                description=form.cleaned_data["ticket_description"],
                image=form.cleaned_data["ticket_image"],
                user=request.user,
            )

            # Créer la critique
            Review.objects.create(
                ticket=ticket,
                headline=form.cleaned_data["review_headline"],
                rating=int(form.cleaned_data["review_rating"]),
                body=form.cleaned_data["review_body"],
                user=request.user,
            )

            messages.success(
                request, "Votre billet et critique ont été créés avec succès!"
            )
            return redirect("feed")
    else:
        form = TicketReviewForm()
    return render(request, "review_create_with_ticket.html", {"form": form})


@login_required
def review_update(request, review_id):
    """Vue de modification d'une critique"""
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre critique a été modifiée avec succès!")
            return redirect("feed")
    else:
        form = ReviewForm(instance=review)
    return render(request, "review_update.html", {"form": form, "review": review})


@login_required
def review_delete(request, review_id):
    """Vue de suppression d'une critique"""
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        messages.success(request, "Votre critique a été supprimée avec succès!")
        return redirect("feed")
    return render(request, "review_confirm_delete.html", {"review": review})


@login_required
def follow_list(request):
    """Vue de la liste des abonnements"""
    following = UserFollows.objects.filter(user=request.user).select_related(
        "followed_user"
    )
    followers = UserFollows.objects.filter(followed_user=request.user).select_related(
        "user"
    )

    context = {
        "following": following,
        "followers": followers,
    }
    return render(request, "follow_list.html", context)


@login_required
def follow_create(request):
    """Vue pour suivre un utilisateur"""
    if request.method == "POST":
        form = UserFollowsForm(request.POST, user=request.user)
        if form.is_valid():
            follow = form.save(commit=False)
            follow.user = request.user
            follow.followed_user = form.cleaned_data["followed_user"]
            follow.save()
            messages.success(
                request, f"Vous suivez maintenant {follow.followed_user.username}!"
            )
            return redirect("follow_list")
    else:
        form = UserFollowsForm(user=request.user)
    return render(request, "follow_create.html", {"form": form})


@login_required
def follow_delete(request, follow_id):
    """Vue pour arrêter de suivre un utilisateur"""
    follow = get_object_or_404(UserFollows, id=follow_id, user=request.user)
    if request.method == "POST":
        username = follow.followed_user.username
        follow.delete()
        messages.success(request, f"Vous ne suivez plus {username}.")
        return redirect("follow_list")
    return render(request, "follow_confirm_delete.html", {"follow": follow})


@login_required
def user_posts(request):
    """Vue des posts de l'utilisateur connecté"""
    tickets = Ticket.objects.filter(user=request.user).annotate(
        content_type=Value("TICKET", CharField())
    )
    reviews = Review.objects.filter(user=request.user).annotate(
        content_type=Value("REVIEW", CharField())
    )

    user_posts = sorted(
        chain(tickets, reviews), key=lambda post: post.time_created, reverse=True
    )

    # Pagination
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request, "user_posts.html", {"posts": posts})
