import pickle
import numpy as np
import json

PRIMES = json.load(open("Generators/PRIMES.json"))

# Charger le modèle
with open('Models/Prem_i.pkl', 'rb') as file:
    model = pickle.load(file)

# Générer les données d'entrée pour les valeurs entre 100 et 200
inputs = np.arange(100, 201).reshape(-1, 1)

# Prédire les résultats
predictions = model.predict(inputs)

# Afficher les résultats
for input_value, prediction in zip(inputs.flatten(), predictions):
    print(f"Input: {input_value}, Prediction: {prediction}")
    
print(list(map(lambda x: PRIMES[x], list(range(100, 201)))))
