import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
stock_symbols = ["AAPL", "TSLA", "MSFT", "GOOGL", "NKE"]

price_change_threshold = 0.25
interval_seconds = 300

API_KEY = os.getenv("API_KEY")
IFTT_WEBHOOK_KEY = os.getenv("IFTT_WEBHOOK_KEY")


historical_prices = "historical price"
seven_day_average = "calcualte seven day average"
IFTT_WEBHOOK_EVENT = "name of event"
avg_price = "average price after 7 days"
calculate_average_price = "average price sum"





def get_stock_price(symbol, API_KEY):
    
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&{symbol}=IBM&apikey={API_KEY}"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo"
    response = requests.get(url)
    data = response.json()
    latest_price = list(data["Time Series(5min)"].values())[0]["4. close"]
    print (float(latest_price))
    return float(latest_price)


for symbol in stock_symbols:
    price = get_stock_price(symbol, API_KEY)
    
        
    
get_stock_price("AAPL", API_KEY)   



for symbol in stock_symbols:
    
    
        
 def send_notification(stock_symbol, current_price, price_change, event):
    IFTT_WEBHOOK_DATA = {
        "value1":stock_symbol,
        "value2":current_price,
        "value3":price_change
    }
    
    url = f"https://maker.ifttt.com/trigger/{IFTT_WEBHOOK_EVENT}/json/with/key/{IFTT_WEBHOOK_KEY}"
    print(event)
    response = requests.post(url, json=IFTT_WEBHOOK_DATA)
    if response.status_code == 200:
        print("notification sent successfully")
    else:
        print("notification sending failed")


while True:
    for symbol in stock_symbols:
        current_price = get_stock_price(symbol) 
        historical_prices[symbol].append(current_price)
        

    if price_change_threshold <= -price_change_threshold:
       send_notification(symbol, current_price,  "stock_price_drop")
    
    
    if current_price < seven_day_average:
       send_notification(symbol, current_price)
       
    if len(historical_prices[symbol]) > 7:
            historical_prices[symbol].pop(0)
        
        
    function = calculate_average_price(symbol)
    if avg_price is not None and current_price < avg_price:
        send_notification(symbol, current_price, f"below 7-day average ({avg_price:.2f})")
            
    time.sleep(300)

