import requests
import matplotlib.pyplot as plt
import datetime

def fetch_bitcoin_prices(days=7):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": str(days)
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

def process_data(data):
    timestamps = []
    prices = []
    
    for point in data['prices']:
        # Convert timestamp from milliseconds to datetime
        time = datetime.datetime.fromtimestamp(point[0] / 1000)
        price = point[1]
        timestamps.append(time)
        prices.append(price)
    
    return timestamps, prices

def plot_prices(dates, prices):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', color='blue')
    plt.title("Bitcoin Price Over Last 7 Days (USD)")
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    raw_data = fetch_bitcoin_prices(days=7)
    
    if raw_data:
        dates, prices = process_data(raw_data)
        plot_prices(dates, prices)