from flask import Flask
app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
   etoiles = ''
    
    for i in range(1, valeur + 1):
        
      etoiles += '' * (valeur - i)
        for j in range(1, i + 1):
           etoiles += str(j)
        for j in range(i - 1, 0, -1):
            etoiles += str(j)
        etoiles += '<br>'
    
   etoiles += '</div>'
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
