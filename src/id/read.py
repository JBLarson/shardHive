
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime
from time import strftime, strptime
import time
from web3 import Web3
import dateparser
import pyetherbalance
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()






ro1, ro2, ro4 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4
)






global infuraUrl

#infuraUrl = 'http://127.0.0.1:7545/'


#addr1 = '0x488CAcDf61724E5698757CB18Dbb698590Ab3b9e'
#addr2 = '0x866BF8f4dc17d48744b6424C2f934799aa9939EA'





infuraUrl = 'https://ropsten.infura.io/v3/8b5812c93ad74ef79e7b9d3420579b0d'

addr1 = '0x9535FC12a7Df5A25Bf4FDF2401a5F727E2914a2e'





def getTransaction(infuraUrl, targetAddress):
        getEthBal0 = pyetherbalance.PyEtherBalance(infuraUrl)
        getEthBal1 = getEthBal0.get_eth_balance(targetAddress)


        return getEthBal1


def priceRn(coin, controlCurrency):
	cg = CoinGeckoAPI()

	controlCurrency, coin = controlCurrency.lower(), coin.lower()
	getCoinData = cg.get_coin_by_id(id=coin, vs_currencies=controlCurrency, local
ization=False)

	lastUpdate = getCoinData['last_updated']
	marketData = getCoinData['market_data']

	ticker = getCoinData['symbol']


	lastPrice = marketData['current_price']['usd']



	parseDate = dateparser.parse(lastUpdate)

	updateTime, updateDate = parseDate.strftime("%X"), parseDate.strftime("%x")

	coin = coin.capitalize()
	#print("\nOn: " + str(str(updateDate)[:5]) + " at: " + str(updateTime) + "  "
 + str(coin) + " Price: $" + str(lastPrice) + "\n")

	priceRnDict = {
		"coin": coin,
		"updateDate": updateDate,
		"updateTime": updateTime,
		"lastPrice": lastPrice
	}

	return priceRnDict


# create time variables
timeRn = datetime.datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))


walletAddr = '0x488CAcDf61724E5698757CB18Dbb698590Ab3b9e' #metamask primary test

walletAddr = '0x866BF8f4dc17d48744b6424C2f934799aa9939EA' #metamask test address #2


ds = priceRn("ethereum", "usd")
ethPriceRn = ds['lastPrice']


#print(metaBalance.keys())


#print(type(metaBalance))


#print("\nRFID Data")
#print('Smart Chip ID: ' + str(id))
#print('Smart Chip Wallet Address: ' + str(walletAddr))


#print("\nWallet Data")






justTime, justDate = strftime("%X"), strftime("%x")
print("\nExecuted Query on: " + str(justDate) + " at: " + str(justTime) + "\n\n")



try:
	#walletAddrz = ['0x90a622ba36714a88d37e4b526f208cc9f981a87d']
	walletAddrz = ['0xf3bab584c3bebbb612533b104c16c019ada33c41']
	metaBalance = getTransaction(infuraUrl, "none")
	for walletAddr in walletAddrz:

		metaBalance = getTransaction(infuraUrl, walletAddr)

		print("\n\nWallet Ending in: " + "  " + str(walletAddr)[-4:])

		currencyBalance = metaBalance['balance']
		currencySymbol = metaBalance['symbol']

		print("Balance: "  + "  " + str(currencyBalance) + "  " + str(currenc
ySymbol))




		print("Current Price of Ethereum:  $" + str(ethPriceRn))
		print("Account Value (USD):  $" + str(ro2(ethPriceRn * int(currencyBa
lance))))


except Exception as e:
	print('\n\nBalance Failed\n\n' + str(e))



justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted Query on: " + str(justDate) + " at: " + str(justTime) + "\n")

