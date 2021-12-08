from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def predition():
    response = ''
    if request.method == 'POST':
        # print(request.form)
        # init_feature = [for x in request.form.values()]

        for i in request.form.values():
            if i == '':
                message = 'veuiller remplir toute les variables '
                return render_template('home.html', error=message)
        print(request.form)

        AGE = int(request.form['AGE'])
        DEPRESSION = int(request.form['DEPRESSION'])
        SEXE = int(request.form['SEXE'])
        CHOLESTEROL = int(request.form['CHOLESTEROL'])
        GAJ = int(request.form['GAJ'])
        TDT = int(request.form['TDT'])
        PAR = int(request.form['PAR'])
        FCMAX = int(request.form['FCMAX'])
        ECG = int(request.form['ECG'])
        PENTE = int(request.form['PENTE'])
        ANGINE = int(request.form['ANGINE'])
        feature = np.append(
            [], [AGE, DEPRESSION, SEXE, CHOLESTEROL, GAJ, TDT, PAR, FCMAX, ECG, PENTE, ANGINE])

        print([feature])
        resulat_prediction = model.predict([feature])
        print(resulat_prediction)
        # print(resulat_prediction)
        if resulat_prediction[0] == 1:
            response = "Vous pouvez etre cardiaque"
        else:
            response = "Vos pouvez ne pas etre cardiaque"
    return render_template('home.html', resp=response, input='')


# @app.route('/')
if __name__ == '__main__':
    app.run(debug=True, port=3000)
