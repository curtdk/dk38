import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
# web3.py instance
w3 = Web3(HTTPProvider("http://localhost:8545"))
print(w3.isConnected())
key="0c2d8c7abe26557777f19ec1df102337c2ac49fd9b621550509b53713a575059"
acct = w3.eth.account.privateKeyToAccount(key)
# compile your smart contract with truffle first  open('./douban.json','w',encoding='utf-8')
# truffleFile = json.load(open('./conr/greeter.json','w',encoding='utf-8'))
truffleFile = json.load(open('./conr/greeter.json'))
abi = truffleFile['abi']
bytecode = truffleFile['data']['bytecode']
contract= w3.eth.contract(bytecode=bytecode, abi=abi)
#building transaction
construct_txn = contract.constructor().buildTransaction({
'from': acct.address,
'nonce': w3.eth.getTransactionCount(acct.address),
'gas': 1728712,
'gasPrice': w3.toWei('21', 'gwei')})
signed = acct.signTransaction(construct_txn)
tx_hash=w3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_hash.hex())
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("Contract Deployed At:", tx_receipt['contractAddress'])