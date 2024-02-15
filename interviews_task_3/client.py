import requests

URL = 'http://localhost:5000'

data = {
    "start_times": [5, 15, 25, 35, 45, 55],
    "end_times": [10, 20, 30, 40, 50, 60]
}

try:
    # Slanje POST zahtjeva prema
    response = requests.post(URL, json=data)

    # Provjera odgovora servera
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.json())

except requests.exceptions.RequestException as e:
    print("Error:", e)

#venv\Scripts\activate
#python client.py