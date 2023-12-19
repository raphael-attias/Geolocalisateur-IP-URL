# Localisateur d'IP en Python

Ce script Python permet de localiser une adresse IP en utilisant l'API gratuite de DbIpCity pour obtenir des informations sur la ville, la région et le pays associés à l'adresse IP. De plus, le script utilise Geopy pour obtenir les coordonnées géographiques (latitude et longitude) de la ville.

## Utilisation

1. Exécutez le script Python.
2. Entrez l'URL ou l'adresse IP que vous souhaitez localiser lorsque le programme le demande.

## Structure du projet

- **main.py**: Le script principal contenant le code source.

## Dépendances

- Python 3.x
- ip2geotools
- geopy

## Informations affichées

Le script affiche les informations suivantes pour l'adresse IP spécifiée :

- Adresse IP
- Ville
- Région
- Pays

S'il est possible de récupérer les coordonnées géographiques, le script affiche également :

- Adresse complète
- Latitude
- Longitude

Note: Assurez-vous d'installer les dépendances en utilisant `pip install ip2geotools geopy` avant d'exécuter le script.

---

**Made in Marseille**

*Contact:* [raphael.attias@laplateforme.io](mailto:raphael.attias@laplateforme.io)
