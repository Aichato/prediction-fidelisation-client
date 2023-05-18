from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def accueil():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        CreditScore = int(request.form['CreditScore'])
        Age = int(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['NumOfProducts'])
        HasCrCard = int(request.form['HasCrCard'])
        IsActiveMember = int(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])
        Geography_Maradi = request.form['Geography_Maradi']
        Geography_Niamey = request.form['Geography_Niamey']
        if(Geography_Maradi == 'Maradi'):
            Geography_Maradi = 1
            Geography_Niamey= 0
            Geography_Tahoua = 0
                
        elif(Geography_Maradi == 'Niamey'):
            Geography_Maradi = 0
            Geography_Niamey= 1
            Geography_Tahoua = 0
        
        else:
            Geography_Maradi = 0
            Geography_Niamey= 0
            Geography_Tahoua = 1
        Gender_Male = request.form['Gender_Male']
        if(Gender_Male == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1

        model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))
        prediction = model.predict([[CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography_Maradi,Geography_Niamey,Gender_Male]])
        if prediction == 1:
             return render_template('index.html',prediction_text="Le client quittera la banque")
        else:
             return render_template('index.html',prediction_text="Le client sera fidéle a la banque")
                
if __name__=="__main__":
    app.run(debug=True)
