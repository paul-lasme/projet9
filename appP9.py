#APP FLASK (commande : flask run)
# Partie formulaire non utilisée (uniquement appel à l'API)

from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from flask_wtf import Form
from wtforms.fields import StringField,BooleanField, PasswordField, TextAreaField
from wtforms.widgets import TextArea
import validators
from wtforms.validators import DataRequired
from toolbox.predict import *
import pandas as pd
import xgboost
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import os
#import socketio



@app.route(/)
def credit(form_id):
   
    #calcul prédiction défaut et probabilité de défaut
    prediction, proba = predict_flask(form_id, dataframe)

    dict_final = {
        'prediction' : 1,
        'proba' : 0
        }

    print('Nouvelle Prédiction : \n', dict_final)

    return jsonify(dict_final)


if __name__ == "__main__":
    app.run(debug=True,port=8080,use_reloader=False)
