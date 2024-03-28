from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def getHealthResult(gender,age):
    print(gender,age)

    # Construct the URL with parameters
    api_url = 'https://health.gov/myhealthfinder/api/v3/myhealthfinder.json'
    params = {'age': age, 'sex': gender}

    
    # Make GET request using requests library
    print('Api url-->',api_url,params)
    response = requests.get(api_url, params=params)
    print('Response-->',response)
        #response.raise_for_status()  # Raise an exception for bad response status
    api_result = response.json()

    
    if api_result:
            heading = api_result['Result']['MyHFHeading']
            resources = api_result['Result']['Resources']['all']['Resource']
            health_info = {'heading': heading, 'resources': []}
            for resource in resources:
               health_info['resources'].append({'title': resource['Title'], 'link': resource.get('AccessibleVersion', '#')})

            return health_info
    else:
            return ""

        # Format response data
        #health_info = {'heading': heading, 'resources': []}
        #for resource in resources:
            #health_info['resources'].append({'title': resource['Title'], 'link': resource.get('AccessibleVersion', '#')})

       # return jsonify(health_info)

  


if __name__ == "__main__":
    print('\n ***Get the Health Info***\n')
    gender = input('\n enter your gender male/female: \n')
    age=input('\n enter your age\n')
    healthdata=getHealthResult(gender,age)
    print("\n")
    pprint(healthdata)
  
