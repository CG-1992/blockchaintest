from web3 import Web3
#import json
#infura_url = "https://mainnet.infura.io/v3/110f5a1533de4693b88ac62a74586a47"
#web3 = Web3(Web3.HTTPProvider(infura_url))
#print(web3.isConnected())
#abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"transferAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":false,"name":"data","type":"bytes"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]')
#address = Web3.toChecksumAddress("0x2392f6abf07b5fce14603d0e28fc952205b8703d")

#contract = web3.eth.contract(address=address, abi = abi)
#print(contract)
#totalSupply = contract.functions.totalSupply().call()
#print(web3.fromWei(totalSupply, "ether"))
#print(contract.functions.name().call())
#print(contract.functions.name().call())
#print(contract.functions.balanceOf('	 0x98c63b7b319dfbdf3d811530f2ab9dfe4983af9d').call())
#print(web3.fromWei(balanceOf, "ether"))

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
account_1 = "0xCa435aedd0CD055D7b2a00435027f38D7616Bd42"
account_2 = "0x7Ea8c649612d912A6571d0De10B1A20f192e1170"
private_key = "8eae086bf69ea235d30167b22afe7aaa40ddf79e68130073efbd82624b138c2c"
# get the nonce
# what is nonce?
## nonce is a number that can only be used once. In cryptography, a nonce is a one-time code selected in a random or pseudo-random manner that is used to securely transmit a main password, preventing replay attacks.
nonce = web3.eth.getTransactionCount(account_1)
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, "ether"),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
#signed transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
#send transaction
#get Transaction hash
