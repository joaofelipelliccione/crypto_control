# REF: https://www.unixtimestamp.com/
from time import timezone
import requests
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

current_year = date.today().year
current_month = date.today().month
current_day = date.today().day
current_hour_utc = datetime.utcnow().hour

today = datetime(
    current_year, current_month, current_day, current_hour_utc, 00, 00
)
today_timestamp_unix = int(today.timestamp())

three_months_ago = today + relativedelta(months=-3)
three_months_ago_timestamp_unix = int(three_months_ago.timestamp())

BTC_USD_ENDPOINT = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={three_months_ago_timestamp_unix}&to={today_timestamp_unix}"

fetched_data = requests.get(BTC_USD_ENDPOINT)
clean_data = fetched_data.json()

last_30_days_prices = clean_data["prices"][59:-1]
last_30_days_market_caps = clean_data["market_caps"][59:-1]

print(last_30_days_prices)
print(last_30_days_market_caps)
