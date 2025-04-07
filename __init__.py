from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)

@app.route('/<int:valeur>')
   resultat = ''
    for i in range(1, valeur + 1):
        # Espaces pour centrer
        resultat += '&nbsp;' * (valeur - i)
        
      
        for j in range(1, i + 1):
            resultat += str(j)
        
     
        for j in range(i - 1, 0, -1):
            resultat += str(j)

        resultat += '<br>'
    
    return resultat

if __name__ == "__main__":
    app.run(debug=True)
