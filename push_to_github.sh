#!/bin/bash
# Script pour pousser le projet vers GitHub
# Remplacez VOTRE_USERNAME par votre nom d'utilisateur GitHub

echo "🚀 Envoi du projet LITReview vers GitHub..."

# Remplacez VOTRE_USERNAME par votre vrai nom d'utilisateur GitHub
GITHUB_USERNAME="VOTRE_USERNAME"
REPO_NAME="OC-Projet9-LITReview"

# Ajouter l'origin remote
git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git

# Pousser vers GitHub
git push -u origin main

echo "✅ Projet envoyé avec succès sur GitHub !"
echo "🌐 Votre dépôt : https://github.com/$GITHUB_USERNAME/$REPO_NAME"
