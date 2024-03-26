from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def getSymptomsResult(userSymptoms):
    pprint(userSymptoms)
    #pprint(os.getenv("My_API_Key"))
    request_url = 'https://symptom-checker4.p.rapidapi.com/analyze'
    payload = {"symptoms": userSymptoms}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key":os.getenv("My_API_Key"),
        "X-RapidAPI-Host": "symptom-checker4.p.rapidapi.com"
    }
    if userSymptoms:
      response = requests.post(request_url, json=payload, headers=headers).json()
      return response
    else :
      return ""

if __name__ == "__main__":
    print('\n ***Get the possible diagnosis***\n')
    usersym = input('\n Enter the symptoms: ')
    #symptomdata = getSymptomsResult(usersym)
    print("\n")
    pprint(symptomdata)
    if "potentialCauses" in symptomdata:
        pprint(symptomdata["potentialCauses"])
    else:
        print("No potential causes found.")
