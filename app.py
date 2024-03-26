from flask import Flask, render_template, request, redirect, url_for
from symptomchecker import getSymptomsResult
from waitress import serve

app = Flask(__name__)

# Store the symptomdata globally to avoid API call on page refresh
symptomdata = None

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('get_symptomchecker'))

@app.route('/Symptomchecker')
def get_symptomchecker():
    global symptomdata
    
    userSymptoms = request.args.get('symptoms')
    if userSymptoms and userSymptoms.strip():  # Check if userSymptoms is not empty
        symptomdata = getSymptomsResult(userSymptoms.strip())
    
    return render_template(
        "Symptomchecker.html",
        symptomdata=symptomdata
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
