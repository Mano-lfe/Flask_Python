from flask import Flask
app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1  # Les deux premiers termes
    suite = []

    for i in range(valeur):
        suite.append(str(a))  # On ajoute le terme actuel à la liste
        a, b = b, a + b       # Mise à jour des deux derniers termes

    # On transforme la liste en chaîne de caractères séparée par des virgules

    return resultat

if __name__ == "__main__":
    app.run(debug=True)
