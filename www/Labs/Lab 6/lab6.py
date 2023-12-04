import requests
import plotly.graph_objects as go
import requests
from random import randint
from datetime import datetime


# Solution for Section 1 - Cat Fact:

res = requests.get("https://catfact.ninja/fact")
j = res.json()
print(j["fact"])

# Solution for Section 3 - Stock Data:

import requests

key = "Z9Y9Q0NGM26CXTZX"
params = {
	"functiion": "TIME_SERIES_DAILY",
	"symbol": "AAPL",
	"apikey": key
}

response = requests.get("https://www.alphavantage.co/query", params = params)
data = response.json()

print(data["Time Series (Daily)"]["2022-11-08"]["1. open"])


# Solution for Section 4:

import plotly.graph_objects as go
import requests
from random import randint

def plot_data(data):
	fig = go.Figure()
	for company in data:
		random_rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
		company_data = data[company]
		fig.add_trace(go.Scatter(
			x = [point[0] for point in company_data],
			y = [point[1] for point in company_data],
			name = company,
			line_color = f"rgb({random_rgb[0]}, {random_rgb[1]}, {random_rgb[2]})",
			opacity = 0.8)
		)

	fig.update_layout(
		title="Timeseries of high price for day",
		xaxis_title="timeseries (daily)",
		yaxis_title="stock price (USD)"
	)
	fig.show()

key = "PSLT6WQ2MQVXL20S"
params = {
	"function": "TIME_SERIES_DAILY",
	"apikey": key
}

data_responses = {}
companies = ["IBM", "GOOGL", "MSFT", "BBY", "TSLA"]

for company_name in companies:
	params["symbol"] = company_name
	response_json = requests.get("https://www.alphavantage.co/query", params = params).json()
	daily = response_json["Time Series (Daily)"]
	data_responses[company_name] = [(date, point['2. high']) for date, point in list(daily.items())[:30]]

plot_data(data_responses)



# # Section 5: 
# # Code will vary by student

