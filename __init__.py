from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(valeur):
        for i in range(1, valeur + 1):
            espaces = '' * (valeur - i)
            etoiles += espaces + '*' * i -
        etoiles += '<br>'
    return etoiles

if __name__ == "__main__":
  app.run(debug=True)
