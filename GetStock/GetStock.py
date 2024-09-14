import re
import requests, time
from bs4 import BeautifulSoup as soup

def stock(x):
    url = 'https://finance.yahoo.com/quote/'+x

    headers = {'User-Agent': 'Mozilla/5.0'}
    webpage = requests.get(url, headers=headers)
    data = soup(webpage.text, 'html.parser')

    company_element = data.find('h1', {'class': 'yf-3a2v0c'})
    if company_element:
        company_nospace = company_element.text.strip()
        get_company = re.search(r'\((.*?)\)', company_nospace)
        if get_company:
            company = get_company.group(1)
    else:
        company = "Company not found"

    price_element = data.find('fin-streamer', {'class': 'livePrice yf-mgkamr'}).span
    if price_element:
        price = price_element.text.strip()
    else:
        price = "Price not found."
    return company, price


stockName = input('input stock name:')
for i in range(11):
    company, price = stock(stockName)
    print(f"Company: {company}")
    print(f"Stock: {price}")
    time.sleep(5)
