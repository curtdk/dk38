from web3 import Web3, HTTPProvider
import ast

address = '0x641dc64BfbcdC419bcc7aFb0cE02D244155e1aC6'
# rpc = 'https://bsc-dataseed1.binance.org:443'
rpc = 'http://localhost:8545'
# rpc = 'https://bsc-dataseed4.ninicoin.io'


Provider = Web3(HTTPProvider(rpc))
# balance = web3.fromWei(web3.eth.getBalance(address), "ether")
# print(balance)


# print(web3.eth.get_block_number());

# addr='0xa90Cd919f8EE03f39B3448413E5289Da80052E99';
addr='0x74bf183F4AA7d9d57b45d513089C06bBda14769C';
# t16_0=web3.eth.get_storage_at(addr,0,);
# tt=web3.eth.get_balance(address)

import binascii
# print (ast.literal_eval(t16_0))
# print ('----------------')
for x in range(0, 10):
    
    a=Provider.eth.get_storage_at(addr,x)
    print(a.hex)
    
# keccak256(key.slot)
from eth_abi.packed import encode_packed
 
 
        # bytes memory slotEncoded  = abi.encodePacked(key,slot);

t_1=encode_packed(['string', 'int'], ("u2", 2))
addr1=Web3.keccak(t_1)
# addr1=Web3.solidity_keccak(t_1)

print(addr1.hex);
a=Provider.eth.get_storage_at(addr,addr1)

print(a)

    
# data = '0x0000000000000000000000000000010000000000000000000000000000000d0c';
# b = parseInt(data.substr(66-1*2,1*2),16);
# c = parseInt(data.substr(66-1*2-16*2,16*2),16);
# d = parseInt(data.substr(66-1*2-16*2-1*2,1*2),16);


# print(web3.eth.get_storage_at(addr,0))
# print(web3.eth.get_storage_at(addr,5))


# '0x5C2C5012e92e69b54B8accf1458202E9e75aBA27'

# web3.eth.get_storage_at('0x5C2C5012e92e69b54B8accf1458202E9e75aBA27', 0)