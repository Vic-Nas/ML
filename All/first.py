from sklearn.feature_extraction.text import CountVectorizer  # Pour transformer le texte en nombres
from sklearn.naive_bayes import MultinomialNB  # Un algorithme simple et efficace
from sklearn.model_selection import train_test_split
import joblib  # Pour sauvegarder le modèle
import numpy as np

# Exemple très simple de données
emails = [
    "Gagnez 1000€ maintenant !!!",
    "Rencontrez des célibataires près de chez vous",
    "Réunion demain à 14h",
    "Félicitations! Vous avez gagné un iPhone",
    "Pouvez-vous relire le rapport ?",
    "N'attendez plus, offre limitée!!!"
]
# 1 = spam, 0 = non spam
labels = [1, 1, 0, 1, 0, 1]

def creer_modele_spam():
    # 1. Transformation du texte en nombres
    # CountVectorizer compte combien de fois chaque mot apparaît
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(emails)

    # 2. Division en données d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, 
        test_size=0.2,  # 20% pour tester
        random_state=42
    )

    # 3. Création et entraînement du modèle
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # 4. Test du modèle
    precision = model.score(X_test, y_test)
    print(f"Précision du modèle: {precision:.2%}")

    return model, vectorizer

def sauvegarder_modele(model, vectorizer, nom_fichier="spam_detector.joblib"):
    """Sauvegarde le modèle et le vectorizer"""
    modele_complet = {
        "model": model,
        "vectorizer": vectorizer
    }
    joblib.dump(modele_complet, nom_fichier)
    print(f"Modèle sauvegardé dans {nom_fichier}")

def charger_modele(nom_fichier="spam_detector.joblib"):
    """Charge le modèle sauvegardé"""
    modele_complet = joblib.load(nom_fichier)
    return modele_complet["model"], modele_complet["vectorizer"]

def predire_spam(texte, model, vectorizer):
    """Prédit si un texte est un spam"""
    # Transforme le nouveau texte en nombres
    X_nouveau = vectorizer.transform([texte])
    # Fait la prédiction
    prediction = model.predict(X_nouveau)
    # Obtient la probabilité
    proba = model.predict_proba(X_nouveau)
    
    est_spam = prediction[0] == 1
    confiance = proba[0][1] if est_spam else proba[0][0]
    
    return est_spam, confiance

if __name__ == "__main__":
    # Création et entraînement du modèle
    print("Création du modèle...")
    model, vectorizer = creer_modele_spam()
    
    # Sauvegarde du modèle
    sauvegarder_modele(model, vectorizer)
    
    # Exemple d'utilisation
    nouveaux_messages = [
        "Salut, on se voit ce soir ?",
        "OFFRE EXCEPTIONNELLE !!! -90% sur TOUT"
    ]
    
    # Test sur de nouveaux messages
    print("\nTest du modèle:")
    for message in nouveaux_messages:
        est_spam, confiance = predire_spam(message, model, vectorizer)
        print(f"\nMessage: {message}")
        print(f"Spam: {'Oui' if est_spam else 'Non'}")
        print(f"Confiance: {confiance:.1%}")