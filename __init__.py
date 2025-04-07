from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
  etoiles = ''
    for j in range(valeur):
      étoiles =''
        for i in range(1, i+1):
            etoiles += '*'
          for i in range(i - 1, 0, -1):
            etoiles += ''
        etoiles += '<br>'
    return etoiles

if __name__ == "__main__":
  app.run(debug=True)
