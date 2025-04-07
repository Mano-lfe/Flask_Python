from flask import Flask
app = Flask(__name__)

@app.route('/<int:n>')
def exercice(n):
    somme = 0
    resultat = f"<h2>Exercice 3 : NOUVEAU</h2>"
    resultat += f"<p>Calcul de la somme des nombres de 1 à {n} selon les conditions suivantes :</p>"
    resultat += "<ul>"
    resultat += "<li>Ajouter à la somme les nombres divisibles par 5 ou 7</li>"
    resultat += "<li>Ignorer les nombres divisibles par 11</li>"
    resultat += "<li>Arrêter si la somme dépasse 5000</li>"
    resultat += "</ul><p>Détails :<br>"

    for i in range(1, n + 1):
        if i % 11 == 0:
            resultat += f"{i} ignoré (divisible par 11)<br>"
            continue
        if i % 5 == 0 or i % 7 == 0:
            somme += i
            resultat += f"{i} ajouté, somme actuelle = {somme}<br>"
        if somme > 5000:
            resultat += "⛔ Somme dépasse 5000, arrêt du programme.<br>"
            break

    resultat += f"</p><p><strong>Somme finale :</strong> {somme}</p>"
    return resultat

if __name__ == "__main__":
    app.run(debug=True)
