import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "litreview.settings")
django.setup()

def create_test_data():
    """Crée des utilisateurs, tickets, reviews et abonnements de test pour LITReview."""
    from django.contrib.auth.models import User
    from litterevu.models import Ticket, Review, UserFollows
    print("Création des données de test...")

    # Créer des utilisateurs de test
    users_data = [
        {
            "username": "alice",
            "email": "alice@example.com",
            "first_name": "Alice",
            "last_name": "Martin",
        },
        {
            "username": "bob",
            "email": "bob@example.com",
            "first_name": "Bob",
            "last_name": "Dupont",
        },
        {
            "username": "charlie",
            "email": "charlie@example.com",
            "first_name": "Charlie",
            "last_name": "Bernard",
        },
    ]

    users = {}
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data["username"],
            defaults={
                "email": user_data["email"],
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
            },
        )
        if created:
            user.set_password("testpass123")
            user.save()
            print(f"✅ Utilisateur créé : {user.username}")
        else:
            print(f"⚠️ Utilisateur existe déjà : {user.username}")
        users[user.username] = user

    # Créer des billets
    tickets_data = [
        {
            "title": "Le Petit Prince - Antoine de Saint-Exupéry",
            "description": "Je recherche des avis sur ce classique de la littérature française. Qu'en avez-vous pensé ?",
            "user": users["alice"],
        },
        {
            "title": "1984 - George Orwell",
            "description": "Roman dystopique incontournable. J'aimerais avoir vos impressions sur l'actualité de ce livre.",
            "user": users["bob"],
        },
        {
            "title": "Clean Code - Robert C. Martin",
            "description": "Livre technique sur les bonnes pratiques de programmation. Utile pour les développeurs ?",
            "user": users["charlie"],
        },
        {
            "title": "L'Alchimiste - Paulo Coelho",
            "description": "Roman philosophique sur la quête de soi. Vos avis sur ce best-seller ?",
            "user": users["alice"],
        },
        {
            "title": "Sapiens - Yuval Noah Harari",
            "description": "Essai sur l'histoire de l'humanité. Que pensez-vous de cette approche de l'histoire ?",
            "user": users["bob"],
        },
    ]

    tickets = []
    for ticket_data in tickets_data:
        ticket, created = Ticket.objects.get_or_create(
            title=ticket_data["title"], defaults=ticket_data
        )
        if created:
            print(f"✅ Billet créé : {ticket.title}")
        else:
            print(f"⚠️ Billet existe déjà : {ticket.title}")
        tickets.append(ticket)

    # Créer des critiques
    reviews_data = [
        {
            "ticket": tickets[0],  # Le Petit Prince
            "rating": 5,
            "headline": "Un chef-d'œuvre intemporel",
            "body": "Le Petit Prince est un livre magnifique qui parle autant aux enfants qu'aux adultes. Les réflexions sur l'amitié, l'amour et la nature humaine sont profondes et touchantes. Saint-Exupéry nous offre une parabole poétique sur la condition humaine.",
            "user": users["bob"],
        },
        {
            "ticket": tickets[0],  # Le Petit Prince
            "rating": 4,
            "headline": "Touchant mais un peu daté",
            "body": "Histoire très belle avec de beaux messages. Quelques passages m'ont semblé un peu moralisateurs, mais l'ensemble reste très touchant. Les illustrations de l'auteur ajoutent beaucoup de charme.",
            "user": users["charlie"],
        },
        {
            "ticket": tickets[1],  # 1984
            "rating": 5,
            "headline": "Troublant d'actualité",
            "body": "Orwell a créé un monde terrifiant qui résonne encore aujourd'hui. La surveillance de masse, la manipulation de l'information... Ce livre est plus que jamais d'actualité. Une lecture indispensable.",
            "user": users["alice"],
        },
        {
            "ticket": tickets[2],  # Clean Code
            "rating": 4,
            "headline": "Excellent pour les développeurs",
            "body": "Robert Martin propose des principes solides pour écrire du code propre et maintenable. Quelques exemples en Java peuvent sembler datés, mais les concepts restent valables. À lire absolument si vous développez.",
            "user": users["alice"],
        },
    ]

    for review_data in reviews_data:
        review, created = Review.objects.get_or_create(
            ticket=review_data["ticket"], user=review_data["user"], defaults=review_data
        )
        if created:
            print(f"✅ Critique créée : {review.headline}")
        else:
            print(f"⚠️ Critique existe déjà : {review.headline}")

    # Créer des relations d'abonnement
    follows_data = [
        {"user": users["alice"], "followed_user": users["bob"]},
        {"user": users["alice"], "followed_user": users["charlie"]},
        {"user": users["bob"], "followed_user": users["alice"]},
        {"user": users["charlie"], "followed_user": users["alice"]},
        {"user": users["charlie"], "followed_user": users["bob"]},
    ]

    for follow_data in follows_data:
        follow, created = UserFollows.objects.get_or_create(
            user=follow_data["user"], followed_user=follow_data["followed_user"]
        )
        if created:
            print(
                f"✅ Abonnement créé : {follow.user.username} suit {follow.followed_user.username}"
            )
        else:
            print(
                f"⚠️ Abonnement existe déjà : {follow.user.username} suit {follow.followed_user.username}"
            )

    print("\n🎉 Données de test créées avec succès !")
    print("\n📝 Comptes de test :")
    print("- alice / testpass123")
    print("- bob / testpass123")
    print("- charlie / testpass123")
    print("- admin / admin123 (superutilisateur)")


if __name__ == "__main__":
    create_test_data()

import os
import django



