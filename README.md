# LITReview - Plateforme de critique de livres et articles

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![License](https://img.shields.io/badge/License-Educational-orange.svg)
![PEP8](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen.svg)
![WCAG](https://img.shields.io/badge/Accessibility-WCAG-blue.svg)

LITReview est une application web Django qui permet aux utilisateurs de demander des critiques de livres ou d'articles et de publier leurs propres critiques.

**🔗 Projet GitHub :** https://github.com/steveraffner/OC-Projet9-LITReview

## 🚀 Fonctionnalités

### Authentification
- Inscription et connexion des utilisateurs
- Système de sessions sécurisé
- Déconnexion

### Gestion des billets (Tickets)
- Création de billets pour demander des critiques
- Modification et suppression de ses propres billets
- Upload d'images (couverture de livre)
- Description détaillée du contenu à critiquer

### Gestion des critiques (Reviews)
- Création de critiques en réponse à des billets
- Création de critiques avec nouveau billet en une fois
- Système de notation de 0 à 5 étoiles
- Modification et suppression de ses propres critiques

### Système d'abonnements
- Suivre/Ne plus suivre d'autres utilisateurs
- Liste des abonnements et abonnés
- Gestion des relations utilisateur

### Flux personnalisé
- Affichage des billets et critiques des utilisateurs suivis
- Affichage de ses propres contenus
- Affichage des critiques en réponse à ses billets
- Tri chronologique inverse (plus récent en premier)
- Pagination

## 🛠️ Technologies utilisées

- **Framework** : Django 5.2
- **Base de données** : SQLite
- **Frontend** : HTML5, CSS3 (design responsive)
- **Python** : 3.8+

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

## 🔧 Installation

### 1. Cloner le projet
```bash
git clone <url-du-repo>
cd litreview
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv

# Sur macOS/Linux
source .venv/bin/activate

# Sur Windows
.venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Effectuer les migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un superutilisateur (optionnel)
```bash
python manage.py createsuperuser
```

### 6. Charger les données de test (optionnel)
```bash
python manage.py loaddata fixtures/test_data.json
```

### 7. Lancer le serveur de développement
```bash
python manage.py runserver
```

L'application sera accessible à l'adresse : http://127.0.0.1:8000

## 👥 Données de test

Le projet inclut des données de test avec :
- 3 utilisateurs de test :
  - `alice` (mot de passe : `testpass123`)
  - `bob` (mot de passe : `testpass123`)
  - `charlie` (mot de passe : `testpass123`)
- 5 billets d'exemple
- 4 critiques d'exemple
- Relations d'abonnement entre utilisateurs

### Connexion avec les comptes de test
1. Allez sur http://127.0.0.1:8000/login/
2. Utilisez un des comptes ci-dessus
3. Explorez les différentes fonctionnalités

## 🎨 Accessibilité (WCAG)

L'application respecte les standards d'accessibilité WCAG :
- Textes alternatifs sur toutes les images
- Structure HTML sémantique (nav, main, article, etc.)
- Labels appropriés sur tous les formulaires
- Contrastes de couleur suffisants
- Navigation au clavier
- Messages d'erreur explicites
- Aria-labels pour améliorer l'expérience avec les lecteurs d'écran

## 📁 Structure du projet

```
litreview/
├── db.sqlite3              # Base de données SQLite
├── manage.py               # Script de gestion Django
├── README.md               # Ce fichier
├── requirements.txt        # Dépendances Python
├── .gitignore             # Fichiers à ignorer par Git
├── media/                 # Fichiers uploadés par les utilisateurs
│   └── tickets/           # Images des billets
├── static/                # Fichiers statiques
│   └── css/
│       └── style.css      # Feuille de style principale
├── templates/             # Templates HTML
│   ├── base.html          # Template de base
│   ├── feed.html          # Flux principal
│   ├── login.html         # Page de connexion
│   ├── signup.html        # Page d'inscription
│   ├── ticket_*.html      # Templates pour les billets
│   ├── review_*.html      # Templates pour les critiques
│   ├── follow_*.html      # Templates pour les abonnements
│   ├── user_posts.html    # Posts de l'utilisateur
│   ├── ticket_snippet.html # Composant billet
│   └── review_snippet.html # Composant critique
├── litreview/             # Configuration Django
│   ├── settings.py        # Configuration principale
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Configuration WSGI
└── litterevu/             # Application principale
    ├── models.py          # Modèles de données
    ├── views.py           # Vues (logique métier)
    ├── forms.py           # Formulaires
    ├── urls.py            # URLs de l'application
    ├── admin.py           # Interface d'administration
    └── migrations/        # Migrations de base de données
```

## 🚀 Déploiement Git

Pour faciliter les déploiements futurs, un script est inclus :

```bash
# Déployer une nouvelle version
./git_deploy.sh "Description des changements"
```

Le script automatise :
- `git add .`
- `git commit -m "message"`
- `git push origin main`

## 📸 Captures d'écran

### Page de connexion
Interface d'authentification accessible avec validation des erreurs

### Flux principal
- Affichage des billets et critiques
- Actions rapides dans la sidebar
- Pagination responsive

### Gestion des billets
- Création avec upload d'images
- Modification et suppression
- Validation des formulaires

### Système de critiques
- Notation par étoiles (0-5)
- Critiques en réponse ou avec nouveau billet
- Affichage du billet associé

### Abonnements
- Liste des utilisateurs suivis
- Gestion des abonnements
- Statistiques d'utilisation

## 🌐 URLs principales

- `/` - Flux principal (authentification requise)
- `/login/` - Page de connexion
- `/signup/` - Page d'inscription
- `/ticket/create/` - Créer un billet
- `/review/create-with-ticket/` - Créer une critique avec billet
- `/follow/` - Gérer les abonnements
- `/my-posts/` - Mes publications

## 📂 Structure GitHub

```
OC-Projet9-LITReview/
├── 📁 litterevu/          # Application Django principale
├── 📁 templates/          # Templates HTML (18 fichiers)
├── 📁 static/css/         # Feuilles de style
├── 📁 media/              # Uploads utilisateur
├── 📄 README.md           # Documentation
├── 📄 requirements.txt    # Dépendances Python
├── 📄 manage.py           # Script Django
├── 📄 create_test_data.py # Données de test
├── 📄 git_deploy.sh       # Script de déploiement
└── 📄 .gitignore          # Fichiers ignorés
```

Ce projet est développé dans le cadre du parcours OpenClassrooms Python.

## 🔒 Sécurité

- Protection CSRF sur tous les formulaires
- Authentification requise pour toutes les actions
- Validation des données côté serveur
- Upload d'images sécurisé
- Clé secrète Django en variable d'environnement (production)

## 🌍 Configuration pour la production

Pour déployer en production :

1. Définir les variables d'environnement :
```bash
export SECRET_KEY="votre-cle-secrete-production"
export DEBUG=False
```

2. Configurer une base de données PostgreSQL ou MySQL

3. Configurer le service de fichiers statiques (AWS S3, etc.)

4. Utiliser un serveur web (Nginx + Gunicorn)

## 🧪 Tests

Pour lancer les tests :
```bash
python manage.py test
```

## 📝 Conformité au code

Le projet respecte les standards PEP8. Pour vérifier :
```bash
flake8 .
```

Pour formater automatiquement :
```bash
black .
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commit vos changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est développé dans le cadre du parcours OpenClassrooms Python.

## 📞 Support

Pour toute question ou problème :
- Ouvrir une issue sur GitHub
- Contacter l'équipe de développement

---

**Développé avec ❤️ en Python & Django par Steve Raffner**
