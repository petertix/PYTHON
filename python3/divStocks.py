import requests
import time
from bs4 import BeautifulSoup  #pip install beautifulsoup4
import pandas as pd

'''
    This script searches for Dividend stocks that yield 8% or more historically.
'''

''' Scrape Data from nasdaq.com website for Dividend Data'''
# Use the Curl to Python web page:
# https://curl.trillworks.com
# https://curlconverter.com/
#
# https://www.nasdaq.com/market-activity/stocks/ibm/dividend-history
#

def readTickers():
    infile  = open('nasdaqList.txt')
    outfile = 'nasdaqSymbols.txt'

    # reading the file as a list line by line
    content = infile.readlines()

    # closing the file
    infile.close()
    #print(content)

    tickers = []
    for x in content:
        a = x.split('|')[0]
        tickers.append(a)

    return(tickers)


if __name__ == '__main__':

    tickers = readTickers()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.nasdaq.com/',
        'Origin': 'https://www.nasdaq.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    params = {
        'assetclass': 'stocks',
    }

    for ticker in tickers:
        response = requests.get(f'https://api.nasdaq.com/api/quote/{ticker}/dividends', params=params, headers=headers, timeout=5)
        response_json = response.json()
        dividend_data = response_json['data']

        if response_json['status']['rCode'] == 200:
 
            dividend_data['dividendPaymentDate']
            dividend_data['dividends'].keys()

            theYield = dividend_data['yield']
            if (theYield != 'N/A'):
                saveYield = theYield
                saveYield = saveYield[:-1]
                numYield = float(saveYield)
                if numYield >10:
                    print(f'{ticker} = {theYield}')

    print('All Done\n')