# REF: https://www.unixtimestamp.com/
import requests
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

current_year = date.today().year
current_month = date.today().month
current_day = date.today().day
today = datetime(current_year, current_month, current_day, 11, 00, 00)
today_timestamp_unix = int(today.timestamp())

three_months_ago = today + relativedelta(months=-3)
three_months_ago_timestamp_unix = int(three_months_ago.timestamp())

start_date_unix = 1648476058
end_date_unix = 1656424858
BTC_USD_ENDPOINT = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={three_months_ago_timestamp_unix}&to={today_timestamp_unix}"

fetched_data = requests.get(BTC_USD_ENDPOINT)
clean_data = fetched_data.json()

print(clean_data["prices"])
