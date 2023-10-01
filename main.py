import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "Twillo sid"
auth_token = "Twillo api auth key"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "API KEY",
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()

if "Time Series (Daily)" in data:
    daily_data = data["Time Series (Daily)"]

    dates = list(daily_data.keys())[:2]

    # Get the data for the past two days
    yesterday_data = daily_data[dates[0]]
    day_before_yesterday_data = daily_data[dates[1]]

    yester_close = float(yesterday_data["4. close"])
    day_before_yestr_close = float(day_before_yesterday_data["4. close"])
    print(yester_close)
    day_before_yestr_close = 300
    print(day_before_yestr_close)
    if yester_close > day_before_yestr_close:
        positive_difference = ((yester_close-day_before_yestr_close)/day_before_yestr_close)*100
    else:
        positive_difference = ((day_before_yestr_close-yester_close)/day_before_yestr_close)*100
    print(positive_difference)

if positive_difference > 5:
    print("Get News")



    parameters2 = {
            "q": "tesla",
            "from": dates[0],
            "apikey": "API KEY",
        }

    response1 = requests.get(NEWS_ENDPOINT, params=parameters2)
    news_data1 = response1.json()


    articles_data = news_data1['articles'][:3]
    news3 = []
    for article in articles_data:
        title = article['title']
        description = article['description']
        news3 += [f"{title} \n \n {description}"]

    print(news3[0])
    print("\n",news3[1])
    print("\n",news3[2])

    client = Client(account_sid, auth_token)

    if yester_close > day_before_yestr_close:

        message = client.messages \
            .create(
            body=f"TSLA 5%🔺📈\n {news3[0]} \n \n {news3[1]} \n\n  {news3[2]}",
            from_="TWILLO PHONE NUMBER",
            to="MY PHONE NUMBER"
        )
        print(message.status)
    else:
        message = client.messages \
            .create(
            body=f"TSLA 5%🔻📉\n {news3[0]} \n \n {news3[1]} \n\n  {news3[2]}",
            from_="TWILLO PHONE NUMBER",
            to="MY PHONE NUMBER"
        )
        print(message.status)

