# Projet de Cryptographie - SDES (Simplified Data Encryption Standard)

Ce projet implémente l'algorithme de cryptographie SDES (Simplified Data Encryption Standard) en Python.  
Il inclut les étapes suivantes :
- Génération des sous-clés
- Permutations initiales et inverses (IP et IP⁻¹)
- Déchiffrement et chiffrement des données

---

## Fonctionnalités

1. **Génération des sous-clés** :
   - Utilisation des permutations P10 et P8
   - Décalage circulaire à gauche (LS-1 et LS-3)

2. **Permutations** :
   - Permutation initiale (IP)
   - Permutation inverse (IP⁻¹)

3. **Chiffrement et Déchiffrement** :
   - Utilisation des sous-clés générées pour chiffrer et déchiffrer un texte clair de 8 bits

---

## Structure du projet


- `sdes.py` : Contient les classes et méthodes principales pour SDES  
- `main.py` : Exemple d'utilisation du chiffrement et déchiffrement  
- `tests/test_sdes.py` : Tests unitaires pour valider le bon fonctionnement des fonctions  

---

## Installation

Assurez-vous d'avoir **Python 3.x** installé sur votre machine.  
Clonez le dépôt et installez les dépendances si nécessaire : 

```bash
git clone https://github.com/M-Isaac-lab/cryptographie.git
cd cryptage
