import requests
import os
import csv

URL = 'https://readthedocs.com/api/v3/projects/morpheus-docs/redirects/'
TOKEN = os.environ.get('APITOKEN')
HEADERS = {'Authorization': f'token {TOKEN}'}

with open('redirect_data.csv') as data_file:
    csv_reader = csv.reader(data_file, delimiter=',')
    for row in csv_reader:
        payload = {
            "from_url": row[0],
            "to_url": row[1],
            "type": "exact",
        }

        response = requests.post(
            URL,
            json=payload,
            headers=HEADERS,
        )

        print(response.json())