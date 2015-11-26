#! /usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup

#Add your own LTC and BTC amounts
LTC = 999
BTC = 999

url = 'http://btc-e.com'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())

btc_eu 	= soup.find(id='last19')
ltc_eu 	= soup.find(id='last27')
ltc_btc	= soup.find(id='last10')

print('\nBTC-e rates:')
print('BTC > EU : ' + btc_eu.string)
print('LTC > EU : ' + ltc_eu.string)
print('LTC > BTC: ' + ltc_btc.string + '\n')

print('EUR(BTC)		: ' + str(BTC*float(btc_eu.string)))
print('EUR(LTC)		: ' + str(LTC*float(ltc_eu.string)))
print('EUR(LTC>BTC)		: ' + str(LTC*float(ltc_btc.string)*float(btc_eu.string)) + '\n')

# Example to link the script to a command
# sudo ln -s /home/<user>/Projects/Crypto_rates/main.py /usr/bin/crypto_rate