# INITIATION-DJANGO

## TD n°1 – Mise en bouche

### Réalisations
1. **Environnement virtuel & installation**  
   - Création d’un virtualenv `~/venv` et activation  
   - Installation de Django avec `pip install django`  
   - Export des dépendances dans `requirements.txt`  

2. **Création du projet**  
   - Commande : `django-admin startproject TutoDjango`  
   - Découverte de la structure (manage.py, settings.py, urls.py, etc.)  

3. **Lancement du serveur**  
   - Démarrage avec `python manage.py runserver`  
   - Accès à `http://127.0.0.1:8000/` → page d’accueil Django  

4. **Base de données**  
   - Configuration par défaut avec SQLite  
   - Migration initiale avec `python manage.py migrate`  
   - Génération du fichier `db.sqlite3`  

5. **Création de l’application**  
   - Commande : `python manage.py startapp monApp`  
   - Ajout de `monApp` dans `INSTALLED_APPS`  

6. **Première vue et routage**  
   - Définition d’une vue `home` dans `monApp/views.py`  
   - Création d’un fichier `monApp/urls.py`  
   - Inclusion des routes dans `TutoDjango/urls.py`  
   - Résultat : affichage de **"Hello Django!"** sur `http://localhost:8000/monApp/`  

7. **Challenge final**  
   - Ajout de deux nouvelles pages : **About Us** et **Contact Us**  
   - Routage dynamique avec un paramètre (`/monApp/home/<nom>`) pour afficher un message personnalisé  
"""