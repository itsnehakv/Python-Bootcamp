import requests
import datetime
import pytz
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


stock_parameters={
"apikey":os.environ["STOCK_APIKEY"],
"symbol":"MSFT",
"function":"TIME_SERIES_DAILY",
"outputsize":"compact"
}
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

response=requests.get(url=f"https://www.alphavantage.co/query",params=stock_parameters)
stock_data=response.json()

#--------Setting the time zone of NASDAQ-------
x=datetime.datetime.now(pytz.timezone("America/New_York")).date()

#-------Getting yesterdays date (data is always from yesterday)----
yesterday_data=d = x - datetime.timedelta(days=1)
print(yesterday_data)

day_before_yesterday_data= yesterday_data - datetime.timedelta(1)

#-------Get closing price of the two days--------
close_yesterday=stock_data["Time Series (Daily)"][str(yesterday_data)]["4. close"]
print(close_yesterday)

close_bfr_yesterday= stock_data["Time Series (Daily)"][str(day_before_yesterday_data)]["4. close"]
print(close_bfr_yesterday)

'''
###ALTERNATE METHOD
*Using list comprehension --> syntax: new_list=[new_item for item in list]

daily_data= stock_data["Time Series (Daily)"]
data_list=[value for (key,value) in daily_data.items()]

A dictionary has been made into a list
O/P: [{1.open.......................},{1...............}]

So, data_list[0]-->yesterdays data, data_list[1]-->day before yesterday 
'''

close_difference=float(close_yesterday)-float(close_bfr_yesterday)

up_or_down= None
if close_difference>0:
    up_or_down="🔺"
else:
    up_or_down="🔻"


perc_close_diff=round((abs(close_difference) / float(close_yesterday))*100)
# print(perc_close_diff)

'''
Q. Why should "close_difference" be an absolute value?
A. Because the "perc_close_diff" needs to be an absolute value, so that
    "if perc_close_diff>0" will be a +ve value which will trigger the news api.
    The increase or decrease in stocks will be infored by "up_or_down" emojis
    
    '''
#-----if 5%+ increase or decrease, then alert user-----
#fetch news articles
if perc_close_diff>0    :
    news_api_id=os.environ["NEWS_APIKEY"]
    news_parameters={
        "apiKey":news_api_id,
        "qInTitle":"Microsoft",
    }
    news_response=requests.get(url=f"https://newsapi.org/v2/everything",params=news_parameters)
    news_data=news_response.json()
    articles=news_data["articles"]
    print(articles)

#------fetching top 3 articles-----
    top_three_articles=articles[:3]
    print(top_three_articles)
# STEP 1: Use https://www.alphavantage.co

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    format_article=[f"Headline:{article["title"]}\n\nBrief:{article["description"]}" for article in top_three_articles]

    for article in format_article:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=f"whatsapp:{os.environ["TWILIO_NUMBER"]}",
            to=f"whatsapp:{os.environ["USER_NUMBER"]}",
            body=f"Microsoft : {perc_close_diff}%{up_or_down}\n{article}"
        )
#....here "article" is just a variable (i.e not actual part of "top_three_articles")
    '''
    #-----top_three_articles --> OUTPUT-->
    [{'source': {'id': 'the-verg...'}, 'author': 'Tom Warren', 'title': 'US nuclear weapons agency reportedly breached in Micro....', 'description': 'Hours after Microsoft revealed hac.....'}, 
    {'source': .......}
    #------So it is a dictionary
    '''