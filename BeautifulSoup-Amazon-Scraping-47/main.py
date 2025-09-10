import ast
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.3",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

Amazon_web=requests.get(url=URL, headers=header)
Amazon_web_txt=Amazon_web.text

soup=BeautifulSoup(Amazon_web_txt,"html.parser")

price_whole=soup.find(name="span",class_="a-price-whole")
price_fraction=soup.find(name="span",class_="a-price-fraction")
product_price=float(price_whole.getText()+price_fraction.getText())

product_title=soup.find(name="span", id="productTitle")
product_name=str(product_title.getText().strip())
# product_name=product_name.replace("b'","").replace("\xc3\xa9","ee")
# product_name_to_bytes=ast.literal_eval(product_name)
# product_name=product_name_to_bytes.decode("utf-8")
SET_PRICE=100

subject = "Amazon Price Alert!"
body = f"{product_name} is now ${product_price}\nBUY AT: {URL}"

msg = MIMEText(body, _charset="utf-8")
msg["Subject"] = subject
msg["From"] = os.environ["SENDER_EMAIL"]
msg["To"] = os.environ["RECEIVER_EMAIL"]

if product_price<SET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:   #w/o "with", connection.close() must be used
        connection.starttls()
        connection.login(user=os.environ["SENDER_EMAIL"],password=os.environ["PASSWORD"])
        connection.sendmail(from_addr=os.environ["SENDER_EMAIL"],to_addrs=os.environ["RECEIVER_EMAIL"],
                            msg=msg.as_string())


'''MIMEText is a class from Python’s email.mime.text module. 
It's used to create text-based email messages that follow the MIME (Multipurpose Internet Mail Extensions)standard
 — the format email clients expect.

MIMEText creates emails that can handle special characters (like é)'''