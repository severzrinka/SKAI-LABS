import requests
import json

def main():
    url = 'http://127.0.0.1:5000'
    
    # Čitanje podataka iz JSON datoteke
    with open('data.json', 'r') as file:
        data = json.load(file)
        
    # Slanje POST zahtjeva na definirani URL s podacima iz JSON datoteke
    response = requests.post(url, json=data)

    print(response.json())

if __name__ == "__main__":
    main()


#venv\Scripts\activate
# python client.py