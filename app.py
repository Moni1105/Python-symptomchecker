from flask import Flask, render_template, request
from symptomchecker import getSymptomsResult
from healthPortal import getHealthResult
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/symptom_checker')
def symptom_checker():
    user_symptoms = request.args.get('symptoms')
    print('User Symptom Variable-->',user_symptoms)
    symptom_data = None
    
    if user_symptoms!=None and user_symptoms.strip():
        print('Inside If condition->',user_symptoms)
        symptom_data = getSymptomsResult(user_symptoms.strip())
    
    return render_template('healthportal.html', symptom_data=symptom_data)

@app.route('/fetch_health_data')
def fetch_health_data():
    gender = request.args.get('gender')
    age = request.args.get('age')
    health_data = None
    print("health response gender age -->",gender,age)
    
    if gender and age:
        health_data = getHealthResult(gender, age)
        print("health response",health_data)
    
    return render_template('healthportal.html', health_data=health_data)
    #return render_template('healthportal.html', heading=health_data['heading'], resources=health_data['resources'])

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
