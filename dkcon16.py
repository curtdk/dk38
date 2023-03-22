from web3.auto import w3

IMPLEMENTATION_SLOT = '0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc'
ADMIN_SLOT = '0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103'
BEACON_SLOT = '0xa3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee59ff6cb3582b35133d50'
OPERATOR_SLOT = '0x14cc265c8475c78633f4e341e72b9f4f0d55277c8def4ad52d79e69580f31482'

def calSlot(str):
    kec = w3.keccak(text=str)
    num = w3.toInt(kec) -1
    result = w3.toHex(num)
    return result

print(calSlot("eip1967.proxy.implementation"));

assert(IMPLEMENTATION_SLOT == calSlot("eip1967.proxy.implementation"))
assert(ADMIN_SLOT == calSlot("eip1967.proxy.admin"))
assert(BEACON_SLOT == calSlot("eip1967.proxy.beacon"))
assert(OPERATOR_SLOT == calSlot("eip1967.proxy.operator"))

print("success")
