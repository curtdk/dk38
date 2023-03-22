import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
# compile your smart contract with truffle first
truffleFile = json.load(open('./contracts/greeter.json'))
abi = truffleFile['abi']
bytecode = truffleFile['data']['bytecode']
# web3.py instance
w3 = Web3(HTTPProvider("http://localhost:8545")) #modify
print(w3.isConnected())
contract_address = Web3.toChecksumAddress("0xee87b241Dd4740D9612B7B798F4e05EEE6487893") #modify
key="0c2d8c7abe26557777f19ec1df102337c2ac49fd9b621550509b53713a575059"#modify
acct = w3.eth.account.privateKeyToAccount(key)
account_address= acct.address
# Instantiate and deploy contract
# contract = w3.eth.contract(abi=abi, bytecode=bytecode)
# Contract instance
contract_instance = w3.eth.contract(abi=abi, address=contract_address)
# Contract instance in concise mode
#contract_instance = w3.eth.contract(abi=abi, address=contract_address, ContractFactoryClass=ConciseContract)
tx = contract_instance.functions.greet("Hello all my goody people").buildTransaction({'nonce': w3.eth.getTransactionCount(account_address)})
#Get tx receipt to get contract address
signed_tx = w3.eth.account.signTransaction(tx, key)
#tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
hash= w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(hash.hex())