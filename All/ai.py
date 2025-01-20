#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error
from joblib import dump
import json
import psutil
import os
import sys

def check_memory():
    """Vérifie si la mémoire disponible est suffisante"""
    available = psutil.virtual_memory().available
    total = psutil.virtual_memory().total
    if available < 0.1 * total:  # Si moins de 10% de mémoire disponible
        raise MemoryError("Mémoire insuffisante pour continuer l'exécution")

def main():
    try:
        # Vérification initiale de la mémoire
        check_memory()
        
        # Charger le fichier JSON et créer le DataFrame initial
        print("Chargement des données...")
        with open("Generators/PRIMES.json", 'r') as f:
            check_memory()
            data = json.load(f)
            
        check_memory()
        df = pd.DataFrame(data, columns=["Target"])
        
        df['Rank'] = df.index
        df = df.sample(frac=1).reset_index(drop=True)
        
        print("Aperçu des données :")
        print(df)

        # Préparation des features (X) et de la cible (y)
        check_memory()
        X = df[['Rank']]
        y = df['Target']

        # Diviser les données
        check_memory()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

        # Définir les paramètres à tester
        print("Configuration de la recherche par grille...")
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [5, 10, 15, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }

        # Initialiser le modèle de base
        base_model = RandomForestRegressor(n_jobs=-1, verbose=0)

        # Initialiser GridSearchCV
        print("Début de la recherche des meilleurs paramètres...")
        check_memory()
        grid_search = GridSearchCV(
            estimator=base_model,
            param_grid=param_grid,
            cv=3,
            n_jobs=-1,
            verbose=2,
            scoring='neg_mean_absolute_error'
        )

        # Effectuer la recherche par grille
        grid_search.fit(X_train, y_train)

        # Afficher les meilleurs paramètres
        print("\nMeilleurs paramètres trouvés:")
        print(grid_search.best_params_)
        print(f"Meilleur score de validation: {-grid_search.best_score_:.3f} (MAE)")

        # Utiliser le meilleur modèle
        best_model = grid_search.best_estimator_

        # Évaluation sur l'ensemble de test
        y_pred = best_model.predict(X_test)
        print(f"\nPerformance sur l'ensemble de test:")
        print(f"R² score: {best_model.score(X_test, y_test)}")
        print(f"MAE: {mean_absolute_error(y_test, y_pred):.3f}")

        # Sauvegarder le meilleur modèle
        dump(best_model, "Models/Prem_i.pkl")
        print("Meilleur modèle sauvegardé avec succès.")

        # Prédictions aléatoires avec le meilleur modèle
        random_ranks = np.random.randint(0, len(df), size=100)
        predictions = {rank: best_model.predict([[rank]])[0] for rank in random_ranks}

        print("\nPrédictions aléatoires avec le meilleur modèle (rang -> nombre premier prédit) :")
        for rank, pred in predictions.items():
            actual = data[rank] if rank < len(data) else None
            print(f"{rank} -> {pred:.0f} (cible réelle : {actual}) -> diff : {abs(pred - actual):.0f}")

    except MemoryError as e:
        print(f"\nERREUR DE MÉMOIRE: {e}")
        print("Le programme s'arrête de manière contrôlée pour éviter de planter le système.")
        sys.exit(1)
    except Exception as e:
        print(f"\nERREUR INATTENDUE: {type(e).__name__}: {e}")
        print("Le programme s'arrête de manière contrôlée.")
        sys.exit(1)

if __name__ == "__main__":
    main()