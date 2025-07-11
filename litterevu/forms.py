from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket, Review, UserFollows


class SignUpForm(UserCreationForm):
    """Formulaire d'inscription personnalisé avec accessibilité"""

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom d'utilisateur",
                "aria-label": "Nom d'utilisateur",
            }
        ),
        label="Nom d'utilisateur",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Mot de passe",
                "aria-label": "Mot de passe",
            }
        ),
        label="Mot de passe",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirmer le mot de passe",
                "aria-label": "Confirmer le mot de passe",
            }
        ),
        label="Confirmer le mot de passe",
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class TicketForm(forms.ModelForm):
    """Formulaire pour créer/modifier un billet"""

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Titre du livre/article",
                    "aria-label": "Titre du livre ou article",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Description de votre demande...",
                    "aria-label": "Description de votre demande de critique",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "aria-label": "Image de couverture du livre (optionnel)",
                }
            ),
        }
        labels = {
            "title": "Titre",
            "description": "Description",
            "image": "Image (optionnel)",
        }


class ReviewForm(forms.ModelForm):
    """Formulaire pour créer/modifier une critique"""

    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]
        widgets = {
            "headline": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Titre de votre critique",
                    "aria-label": "Titre de votre critique",
                }
            ),
            "rating": forms.Select(
                choices=[(i, f'{i} étoile{"s" if i > 1 else ""}') for i in range(6)],
                attrs={"class": "form-select", "aria-label": "Note de 0 à 5 étoiles"},
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Votre critique détaillée...",
                    "aria-label": "Contenu détaillé de votre critique",
                }
            ),
        }
        labels = {"headline": "Titre", "rating": "Note", "body": "Critique"}


class TicketReviewForm(forms.Form):
    """Formulaire pour créer un billet ET une critique en même temps"""

    # Champs pour le ticket
    ticket_title = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Titre du livre/article",
                "aria-label": "Titre du livre ou article",
            }
        ),
        label="Titre du livre/article",
    )
    ticket_description = forms.CharField(
        max_length=2048,
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Description du livre/article...",
                "aria-label": "Description du livre ou article",
            }
        ),
        label="Description",
    )
    ticket_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "aria-label": "Image de couverture du livre (optionnel)",
            }
        ),
        label="Image (optionnel)",
    )

    # Champs pour la critique
    review_headline = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Titre de votre critique",
                "aria-label": "Titre de votre critique",
            }
        ),
        label="Titre de la critique",
    )
    review_rating = forms.ChoiceField(
        choices=[(i, f'{i} étoile{"s" if i > 1 else ""}') for i in range(6)],
        widget=forms.Select(
            attrs={"class": "form-select", "aria-label": "Note de 0 à 5 étoiles"}
        ),
        label="Note",
    )
    review_body = forms.CharField(
        max_length=8192,
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Votre critique détaillée...",
                "aria-label": "Contenu détaillé de votre critique",
            }
        ),
        label="Critique",
    )


class UserFollowsForm(forms.ModelForm):
    """Formulaire pour suivre un utilisateur"""

    followed_user = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom d'utilisateur à suivre",
                "aria-label": "Nom d'utilisateur à suivre",
            }
        ),
        label="Utilisateur à suivre",
    )

    class Meta:
        model = UserFollows
        fields = ["followed_user"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean_followed_user(self):
        username = self.cleaned_data["followed_user"]

        # Vérifier que l'utilisateur existe
        try:
            followed_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.")

        # Vérifier qu'on ne se suit pas soi-même
        if followed_user == self.user:
            raise forms.ValidationError("Vous ne pouvez pas vous suivre vous-même.")

        # Vérifier qu'on ne suit pas déjà cet utilisateur
        if UserFollows.objects.filter(
            user=self.user, followed_user=followed_user
        ).exists():
            raise forms.ValidationError("Vous suivez déjà cet utilisateur.")

        return followed_user
