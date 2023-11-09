# Sentiment Analysis with Twitter API

Ce programme collecte des tweets en utilisant l'API Twitter, les prétraite, extrait des fonctionnalités, entraîne un modèle de classification de sentiment et l'utilise pour prédire le sentiment de nouveaux tweets.

## Installation

1. Clonez le dépôt GitHub :
git clone https://github.com/votre-utilisateur/mon-projet.git

2. Installez les dépendances :
pip install tweepy textblob scikit-learn


## Configuration

Avant d'exécuter le programme, vous devez configurer les identifiants de l'API Twitter dans le fichier `main.py`.

```python
# API credentials
API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

## Utilisation
Exécutez le programme :
python main.py

Le programme collectera des tweets contenant le mot clé "Gabon" à partir de l'API Twitter, les prétraitera, extraira des fonctionnalités, entraînera un modèle de classification de sentiment et l'utilisera pour prédire le sentiment de nouveaux tweets.
Exigences supplémentaires
Ce programme nécessite une connexion Internet pour accéder à l'API Twitter. Assurez-vous d'avoir une clé d'API Twitter valide avant de l'exécuter.

## Contributing
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request pour améliorer ce programme.

## License
Ce programme est sous licence MIT. Voir le fichier LICENSE pour plus de détails.


Ce fichier `README.md` fournit une brève description du programme, des instructions d'installation, de configuration et d'utilisation, des exigences supplémentaires, des informations sur la contribution et la licence.

Veuillez personnaliser ce fichier `README.md` en fonction de votre projet spécifique.

