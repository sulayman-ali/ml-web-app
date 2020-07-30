from flask import Flask, render_template, request
from sklearn.externals import joblib
import requests
import pandas as pd 
import numpy as np 

app = Flask(__name__)

#Load model_prediction


@app.route("/")
def home():
	return render_template('home.html')

@app.route("/predict", methods = ["GET","POST"])
def predict():
	if request.method == "POST":
		try:
			NewYork = float(request.form["NewYork"])
			California = float(request.form["California"])
			Florida = float(request.form["Florida"])
			RnD_Spend = float(request.form["RnD_Spend"])
			Administration = float(request.form["Administration"])
			MarketingSpend = float(request.form["MarketingSpend"])
			pred_args = np.array([
				RnD_Spend,Administration,MarketingSpend,
				NewYork,California,Florida
				]).reshape(1,-1)

			ml_reg = open("multiple_linear_model.pkl","rb")
			ml_model = joblib.load(ml_reg)
			model_prediciton = ml_model.predict(pred_args)
			model_prediction = round(float(model_prediciton))
		
		except ValueError:
			return "Please check if values are entered correctly"

	return render_template('predict.html', prediction = round(float(model_prediciton)))


if __name__ == "__main__":
	app.run(host='0.0.0.0') 