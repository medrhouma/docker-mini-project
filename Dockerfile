
# Image Python avec version explicite
FROM python:3.12-slim

# Répertoire de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

# Port de l'application
EXPOSE 5000

# Variables par défaut
ENV APP_MESSAGE="Bienvenue dans mon projet Docker"
ENV APP_VERSION="1.0.1"

# Démarrage de l'application
CMD ["python", "app.py"]
