from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
   nombres = ''   
    for i in range(1, valeur + 1):
        
      nombres += '' * (valeur - i)
        for j in range(1, i + 1):
           nombres += (j)
        for j in range(i - 1, 0, -1):
            nombres += str(j)
        nombres += '<br>'
    return nombres

if __name__ == "__main__":
    app.run(debug=True)
