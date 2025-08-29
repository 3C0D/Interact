# Projet d'Interface IA

## Développement

### Étape 1 : Mise en place de l'environnement

- Création de l'environnement virtuel Python:

  ```powershell
  python -m venv venv # Attention ne faire qu'une fois!
  ```

- Installation des dépendances (PyQt6, google-generativeai):

  ```powershell
  .\venv\Scripts\activate
  pip install -r requirements.txt
  ```

  Une fois activé, lancez l'application avec `python main.py`.
- Structure des dossiers :
  - `ui/` pour les interfaces
  - `ia_integration/` pour les connexions aux API d'IA
  - `core/` pour la logique métier
  - `data_persistence/` pour la gestion des données

### Étape 2 : Fonctionnalités implémentées

- Création d'une fenêtre principale avec Qt6.
- Ajout des éléments d'interface :
  - Zone de texte pour les prompts.
  - Bouton d'envoi.
  - Zone d'affichage des réponses.
- Intégration avec l'API Gemini.
- Sélection du modèle Gemini via un menu déroulant.
- Persistance de l'historique des conversations pendant la durée de vie de la fenêtre.

### Prochaines étapes

- Ajout de fonctionnalités supplémentaires.
- Personnalisation de l'interface.

## Historique des modifications

### 2024-07-30 - Amélioration 2

- **Nouvelle fonctionnalité** : Support multimodal pour l'intégration d'images
  - Ajout de boutons pour sélectionner et effacer des images
  - Prévisualisation des images sélectionnées dans l'interface
  - Envoi d'images avec les prompts vers l'API Gemini
  - Support des formats : PNG, JPG, JPEG, GIF, BMP
- **Dépendances** : Ajout de Pillow pour le traitement des images

### 2024-07-30 - Amélioration 1

- **Fonctionnalités implémentées**:
  - Persistance de l'historique des conversations pendant la durée de vie de la fenêtre.
  - Sélection du modèle Gemini via un menu déroulant.
- **Refactoring**:
  - Renommage de `README.md` en `HISTORY.md` pour mieux refléter son rôle de journal des modifications.
  - Création d'un nouveau `README.md` avec une brève description du projet et un lien vers `HISTORY.md`.
  - Mise à jour des règles du projet dans `.trae/rules/project_rules.md` pour inclure les directives sur l'utilisation du dossier `Windows_and_Linux` et la gestion de l'historique.

### 2024-07-30 - Correction de bug

- **Bug corrigé** : Résolution du `TypeError` lors du collage d'une image dans la zone de prompt, causé par une mauvaise construction de `QKeyEvent` dans `ui/main_window.py`.

### 2024-07-30 - Amélioration 3

- **Amélioration UI** : Le texte du bouton "Select Image" a été modifié en "Select Image (or Paste above)" pour indiquer la possibilité de coller des images directement dans la zone de prompt.

## Notes

Ce document sera mis à jour au fur et à mesure du développement du projet.

## Spécifications pour les LLM reprenant le projet

Lors de la reprise de ce projet par un autre modèle de langage (LLM), veuillez prendre en compte les points suivants :

- **Contexte de l'environnement :** Le projet est développé sous Windows 11. Les commandes shell doivent être compatibles avec PowerShell.
- **Langue de communication :** La communication avec l'utilisateur doit se faire en français.
- **Langue des commentaires et explications du code :** Les commentaires et explications dans le code doivent être en anglais.
- **Concision :** Soyez concis dans les réponses, mais prêt à fournir plus de détails si demandé.
- **Auto-acceptation des changements :** Les changements en mode 'builder' doivent être auto-acceptés.
- **Navigation des dossiers :** Vous avez la permission de visiter les dossiers parents pour une meilleure compréhension de la structure du projet.
- **Gestion des dépendances :** Assurez-vous que l'environnement virtuel est activé et que toutes les dépendances listées dans `requirements.txt` sont installées avant d'exécuter le projet.
- **Débogage :** En cas d'erreur `ModuleNotFoundError`, vérifiez l'activation de l'environnement virtuel et la présence des modules dans `requirements.txt`.
