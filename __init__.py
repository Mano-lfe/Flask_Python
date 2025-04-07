from flask import Flask
app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    resultat = ''
    for i in range(1, valeur + 1):
        # Espaces pour centrer
        resultat += '&nbsp;' * (valeur - i)
        
        # Nombres croissants
        for j in range(1, i + 1):
            resultat += str(j)
        
        # Nombres décroissants
        for j in range(i - 1, 0, -1):
            resultat += str(j)

        # Saut de ligne HTML
        resultat += '<br>'
    
    return resultat

if __name__ == "__main__":
    app.run(debug=True)
