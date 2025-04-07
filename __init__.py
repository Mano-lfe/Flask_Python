from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(_name_)

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1
    count = [str(0)] 

    if valeur > 1:
        count.append(str(b))

    for _ in range(2, valeur):
        c = a + b
        count.append(str(c))
        a, b = b, c

    return ', '.join(count)  

if _name_ == "_main_":
    app.run(debug=True)
