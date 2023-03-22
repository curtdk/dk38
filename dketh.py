import requests
import json

url = "http://sample-endpoint-name.network.quiknode.pro/token-goes-here/"

payload = json.dumps({
  "method": "eth_getStorageAt",
  "params": [
    "0xE592427A0AEce92De3Edee1F18E0157C05861564",
    "0x0",
    "latest"
  ],
  "id": 1,
  "jsonrpc": "2.0"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
