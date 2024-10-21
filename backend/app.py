from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from polygon import RESTClient  # Make sure to install this package if you're using it
import os

app = Flask(__name__)

# Load the trained model
model = load_model('my_model.h5')

# Set up your Polygon API key
API_KEY = 'Zp7hFhaLuHUYViMTJnyxakcEoKAmVfiY'  # Replace with your actual Polygon API key
client = RESTClient(API_KEY)

def fetch_stock_data(symbol):
    # Fetch historical stock data for the given symbol
    try:
        # Adjust the date range as needed
        data = client.stocks_equities_aggregates(symbol, 1, "day", "2023-01-01", "2023-12-31", unadjusted=True)
        df = pd.DataFrame(data['results'])  # Convert results to a DataFrame
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def preprocess_data(df):
    # Preprocess the stock data for your model
    # Example: Normalize or standardize the data
    # You may need to adjust the input shape based on your model's requirements
    # Here, we're assuming the model takes 'open', 'high', 'low', 'close' prices as input
    X_input = np.array(df[['open', 'high', 'low', 'close']])
    return X_input

@app.route('/predict', methods=['POST'])
def predict():
    # Get the stock symbol from the request
    data = request.json
    symbol = data.get('symbol')

    # Fetch stock data
    stock_data = fetch_stock_data(symbol)
    if stock_data is None or stock_data.empty:
        return jsonify({"error": "Failed to fetch stock data"}), 400
    
    # Preprocess the stock data
    X_input = preprocess_data(stock_data)

    # Predict the stock price
    prediction = model.predict(X_input)

    return jsonify({
        'mean': prediction[0][0].tolist(),
        'lower': prediction[0][1].tolist(),
        'upper': prediction[0][2].tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)
