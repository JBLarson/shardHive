

from web3 import Web3
import json
#from web3.auto import w3


print('\n')


ganache_url = 'https://ropsten.infura.io/v3/8b5812c93ad74ef79e7b9d3420579b0d'
web3 = Web3(Web3.HTTPProvider(ganache_url))
account_1 = '0x2C2E5b824EA2BcE625943aF15e1bBD86630B37EF'
private_key1 = '573b5e055d936fdffe337aa5104aaf73c9d1f1659cad2f07fd924a0ec85fc98d'
account_2 = '0x983C36a518c56b0FCE99AA8a4aed40913DC469CE'


contractAddress = '0xa51b997E0203136b4fA8c1017829aB8E77eE0b6E'

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(account_1)

#cNonce = web3.eth.getTransactionCount(contractAddress)

#print(nonce)
#print(cNonce)

EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501


#jb3 = web3.eth.contract(address=account_2, abi=EIP20_ABI)


jb3 = web3.eth.contract(address=contractAddress, abi=EIP20_ABI)


# Build a transaction that invokes this contract's function, called transfer
jb3_txn = jb3.functions.transfer(
	account_2,
	10000,
	).buildTransaction({
	'chainId': 3,
	'gas': 100000,
	'maxFeePerGas': web3.toWei('2', 'gwei'),
	'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
	'nonce': nonce,
})


print(jb3_txn)

try:

	#sign the transaction
	signed_tx = web3.eth.account.sign_transaction(jb3_txn, private_key=private_key1)
	#print(signed_tx)


except Exception as e:
	print(e)



print()

try:

	#send transaction
	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	#get transaction hash
	print(web3.toHex(tx_hash))

	tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
	print(tx_receipt)

except Exception as e:
	print(e)




print('\n')
