#APP FLASK (commande : flask run)
# Partie formulaire non utilisée (uniquement appel à l'API)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def credit():
   
    #calcul prédiction défaut et probabilité de défaut
    #prediction, proba = predict_flask(form_id, dataframe)

    dict_final = {
        'prediction' : 1,
        'proba' : 0
        }

    print('Nouvelle Prédiction : \n', dict_final)

    return jsonify(dict_final)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True,port=8080,use_reloader=False)