from flask import Flask, render_template, request, jsonify
import pandas as pd
from joblib import dump, load
import json
#from jinja2.utils import escape
# Resto de tu código aquí


with open('diabetesCLasificacion.joblib','rb') as f:
    model = load(f)

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('index.html')
    # Asegúrate de guardar los resultados en variables
    #if request.method == 'GET':
    

    #if request.method == 'POST':
        

  #  return render_template('index.html', original_input={
   #             'glucose': Glucose,
    #            'bloodPressure': BloodPressure,
     #           'insulin': Insulin,
      #          'bmi': bMI,
       #         'diabetesPedigreeFunction': DiabetesPedigreeFunction,
        #        'age': Age
         #   }, result=predictions )
         # Imprimir la predicción
      
    
@app.route('/predicted', methods=['POST'])
def predict():
    try:
        data = json.loads(request.data.decode('utf-8'))  # Lee los datos JSON de la solicitud
        Glucose = float(data['Glucose'])
        BloodPressure = float(data['BloodPressure'])
        Insulin = float(data['Insulin'])
        BMI = float(data['BMI'])
        DiabetesPedigreeFunction = float(data['DiabetesPedigreeFunction'])
        Age = float(data['Age'])
        
        poner_var = pd.DataFrame([[Glucose, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age]],
                                  columns=['Glucose', 'BloodPressure', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        
        predictions = model.predict(poner_var)
        print(predictions)

        if predictions[0] == 1:
            resultado = 'El modelo predice que tiene diabetes.'
            print("El modelo predice que tiene diabetes.")
        else:
            resultado = 'El modelo predice que no tiene diabetes.'
            print("El modelo predice que no tiene diabetes.")
        
        response_data = {'resultado': resultado}
        return jsonify(response_data), 200  # Devuelve una respuesta JSON con código 200 (OK)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Devuelve una respuesta JSON con código 400 (Bad Request) en caso de error
'''  ***
@app.route('/predicted', methods=['POST'])
def predict():
        Glucose=float(request.form['Glucose'])
        BloodPressure=float(request.form['BloodPressure'])
        Insulin=float(request.form['Insulin'])
        bMI=float(request.form['BMI'])
        DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
        Age=float(request.form['Age'])
        poner_var= pd.DataFrame([[Glucose, BloodPressure, Insulin, bMI, DiabetesPedigreeFunction, Age]],
                               columns=['Glucose', 'BloodPressure', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        predictions=model.predict(poner_var)
        print(predictions)

        if predictions[0] == 1:
            datos = {'resultado': 'El modelo predice que tiene diabetes.'}
            print("El modelo predice que tiene diabetes.")
        else:
            datos = {'resultado': 'El modelo predice que no tiene diabetes.'}
            print("El modelo predice que no tiene diabetes.")
        return datos
'''
if __name__ == '__main__':
    app.run(debug=True)
