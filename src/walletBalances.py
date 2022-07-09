

from time import strftime, strptime
import pyetherbalance
from pycoingecko import CoinGeckoAPI
from shardFuncs import *
from infuraUrl import infuraUrl
from secrets import pubKeys

# lambda functions for rounding
ro1, ro2, ro4 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4)


global infuraUrl



def getTransaction(infuraUrl, targetAddress):
        getEthBal0 = pyetherbalance.PyEtherBalance(infuraUrl)
        getEthBal1 = getEthBal0.get_eth_balance(targetAddress)
        return getEthBal1


def priceRn(coin, controlCurrency):
	cg = CoinGeckoAPI()
	controlCurrency, coin = controlCurrency.lower(), coin.lower()
	getCoinData = cg.get_coin_by_id(id=coin, vs_currencies=controlCurrency, localization=False)
	marketData = getCoinData['market_data']
	lastPrice = marketData['current_price']['usd']
	coin = coin.capitalize()

	priceRnDict = {"coin": coin, "lastPrice": lastPrice}

	return priceRnDict



def fetchWalletBalance(walletAddr):
	try:
		ethPriceRn = priceRn("ethereum", "usd")['lastPrice']
		metaBalance = getTransaction(infuraUrl, walletAddr)

		currencyBalance = ro4(metaBalance['balance'])
		currencySymbol = metaBalance['symbol']
		balanceUsd = ro2(currencyBalance * ethPriceRn)

		walletResponse = {'wallet': walletAddr[-4:], 'balETH': currencyBalance, 'balUSD': balanceUsd}


	except Exception as e:
		print('\n\nFetching Balance Failed\nError Msg in Response\n\n')
		walletResponse = {'wallet': walletAddr, 'error': str(e)}

	return walletResponse



doloresWallet, jTestWallet, shardHiveWallet = pubKeys['dolores'], pubKeys['jTest'], pubKeys['shardHive']


justTime, justDate = strftime("%X"), strftime("%x")
print("\nExecuted Query on: " + str(justDate) + " at: " + str(justTime) + "\n")


doloresBalance, jTestBalance, shardHiveBalance = fetchWalletBalance(doloresWallet), fetchWalletBalance(jTestWallet), fetchWalletBalance(shardHiveWallet)

print("Dolores: " + str(doloresBalance) + "\njTest: " + str(jTestBalance)+ "\nshardHive: " + str(shardHiveBalance))


justDate = justDate.replace('/', ':')
currentDT = str(justDate) + "_" + str(justTime)
testAcctBalances = {'dt': currentDT, 'jTest': jTestBalance, 'dolores': doloresBalance, 'shardHive': shardHiveBalance}


jsonOutAddr = 'walBals/' + str(currentDT) + '.json'


try:
	writeTestBalances = writeJson(jsonOutAddr, testAcctBalances)
	print("\n" + str(writeTestBalances))
except Exception as e:
	print('\nFailed to write test balances. error msg below\n')
	print(e)


justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted Query on: " + str(justDate) + " at: " + str(justTime) + "\n")
