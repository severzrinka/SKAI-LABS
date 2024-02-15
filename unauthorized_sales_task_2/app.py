from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def detect_unauthorized_sales():
    try:
        data = request.json
        # Provjera valjanosti podataka
        if not data or 'productListings' not in data or 'salesTransactions' not in data:
            return jsonify({"error": "Invalid input. Both productListings and salesTransactions must be provided."}), 400
        
        # Izvlačenje informacija o produktima i transakcijama iz dobivenih podataka
        product_listings = {item['productID']: item['authorizedSellerID'] for item in data['productListings']}
        sales_transactions = {(item['productID'], item['sellerID']) for item in data['salesTransactions']}
        
        # Pronalaženje neovlaštenih prodaja
        unauthorized_sales = []
        for product_id, seller_id in sales_transactions:
            if product_id in product_listings and seller_id != product_listings[product_id]:
                unauthorized_sales.append({"productID": product_id, "unauthorizedSellerID": [seller_id]})
        
        return jsonify({"unauthorizedSales": unauthorized_sales}), 200
    except Exception as e:
        # Ako se dogodi bilo koja greška tijekom izvršavanja
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

#venv\Scripts\activate
#python app.py