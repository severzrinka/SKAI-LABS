from flask import Flask, request, jsonify

app = Flask(__name__)

# Funkcija koja računa maksimalan broj neprekidnih intervjua
def max_non_overlapping_interviews(start_times, end_times):
    # Provjera da li su liste start_times i end_times iste dužine
    if len(start_times) != len(end_times):
        return 400, "Start times and end times lists must be of equal length"

    # Spajanje početnih i završnih vremena intervjua i sortiranje po završnim vremenima
    interview_times = sorted(zip(start_times, end_times), key=lambda x: x[1])
    
    max_interviews = 0 # Inicijalno postavljamo maksimalan broj intervjua na 0
    last_end_time = float('-inf') # Zadnje završno vrijeme postavljamo na negativnu beskonačnost

    # Iteracija kroz sve intervjue
    for start, end in interview_times:
        # Provjera da li trenutni intervju počinje nakon završetka prethodnog
        if start >= last_end_time:
            max_interviews += 1 # Ako je to slučaj, povećavamo broj maksimalnih intervjua
            last_end_time = end # Postavljamo završno vrijeme trenutnog intervjua kao zadnje završno vrijeme
    
    return 200, {"max_interviews": max_interviews} # Vraćamo uspješan status i rezultat

@app.route('/', methods=['POST'])
def calculate_max_interviews():
    try:
        # Dobivanje JSON podataka iz zahtjeva
        data = request.get_json()
        start_times = data.get('start_times', []) # Lista početnih vremena intervjua
        end_times = data.get('end_times', []) # Lista završnih vremena intervjua
        # Pozivanje funkcije za računanje maksimalnog broja intervjua
        status_code, response = max_non_overlapping_interviews(start_times, end_times)
        return jsonify(response), status_code # Vraćanje rezultata kao JSON i status koda
    except Exception as e:
        return jsonify({"error": str(e)}), 400 # Vraćanje greške ako dođe do iznimke

if __name__ == '__main__':
    app.run(debug=True)


#venv\Scripts\activate
#python app.py