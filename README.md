# Predictify 📈🔮

## Inspiration 💡
The stock market's unpredictability has always been a challenge for investors. We were inspired to create Predictify to harness the power of machine learning and provide a tool that could offer insights into future stock prices, helping both novice and experienced investors make more informed decisions.

## What it Does 🚀
Predictify is a stock price prediction tool that:
- Fetches real-time stock data using the Polygon API 📊
- Utilizes a deep learning model (LSTM) to predict future stock prices 🧠
- Provides a range of predicted prices, offering a more comprehensive outlook 📉📈
- Visualizes historical data and predictions for easy interpretation with graphs 📈
- Allows users to input any stock symbol for analysis 💼

## How We Built It 🛠️
We built Predictify using a combination of powerful tools and technologies:
- **Python**: The core language for our project 🐍
- **TensorFlow**: For building and training our LSTM model 🤖
- **Polygon API**: To fetch real-time and historical stock data 📡
- **Pandas & NumPy**: For data manipulation and analysis 🐼🔢
- **Matplotlib**: For creating visualizations 📊
- **Scikit-learn**: For data preprocessing and model evaluation 🧪

### Our Model Architecture:
```plaintext
LSTM(50, return_sequences=True)
LSTM(50)
Dense(25)
Dense(3)  # Outputs mean, lower, and upper bounds
