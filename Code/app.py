from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = joblib.load('modelo/predirenta.pkl')
scaler = joblib.load('modelo/escalador.pkl')

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"})

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"success": False, "message": 'No selected file'})
    
    if file and file.filename.endswith('.csv'):
        try:
            df = pd.read_csv(file)
            df.columns = df.columns.str.strip()
            print(df.columns)
            if 'Items_Available' not in df.columns or 'Daily_Customer_Count' not in df.columns:
                return jsonify({"success": False, "message": 'El archivo CSV no contiene las columnas necesarias'})
            
            df['Items_Per_Customer'] = df['Items_Available'] / df['Daily_Customer_Count']
            df['Items_Per_Area'] = df['Items_Available'] / df['Store_Area']
            df['Items_Area_Interaction'] = df['Items_Available'] * df['Store_Area']
            df['Sales_Per_Customer'] = df['Store_Sales'] / df['Daily_Customer_Count']
            df['Sales_Per_Item'] = df['Store_Sales'] / df['Items_Available']

            X = df[['Items_Available', 'Daily_Customer_Count', 'Store_Area', 'Items_Per_Customer',
                    'Items_Per_Area', 'Items_Area_Interaction', 'Sales_Per_Customer', 'Sales_Per_Item']]
            X_scaled = scaler.transform(X)

            predictions = model.predict(X_scaled)

            profitability_threshold = 45000
            result = "Rentable" if predictions[0] > profitability_threshold else "No es rentable"
            
            return jsonify({"success": True, "predicción": result, "valor_predicción": predictions[0]})

        except Exception as e:
            return jsonify({"success": False, "message": str(e)})

    else:
        return jsonify({"success": False, "message": "Por favor, sube un archivo CSV válido"})

if __name__ == '__main__':
    app.run(debug=True)