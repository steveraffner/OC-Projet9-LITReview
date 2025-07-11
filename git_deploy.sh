#!/bin/bash

# Script de déploiement Git pour LITReview
# Usage: ./git_deploy.sh "message de commit"

# Couleurs pour l'affichage
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Déploiement Git en cours...${NC}"

# Vérifier si un message est fourni
if [ -z "$1" ]; then
    echo -e "${RED}❌ Erreur: Veuillez fournir un message de commit${NC}"
    echo "Usage: ./git_deploy.sh \"Votre message de commit\""
    exit 1
fi

# Ajouter tous les fichiers
echo -e "${BLUE}📁 Ajout des fichiers...${NC}"
git add .

# Vérifier s'il y a des changements
if git diff --staged --quiet; then
    echo -e "${RED}ℹ️  Aucun changement à commiter${NC}"
    exit 0
fi

# Commit avec le message fourni
echo -e "${BLUE}💾 Création du commit...${NC}"
git commit -m "$1"

# Push vers GitHub
echo -e "${BLUE}📤 Push vers GitHub...${NC}"
git push origin main

echo -e "${GREEN}✅ Déploiement terminé avec succès !${NC}"
echo -e "${GREEN}🌐 Votre projet est disponible sur : https://github.com/steveraffner/OC-Projet9-LITReview${NC}"
