import http.client
import mimetypes
from codecs import encode

def game1(N):
    conn = http.client.HTTPSConnection("ht.srtt.nctian.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=action;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("批量通过"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=opers;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("ad_lnsh"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=record[];'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("3070184"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=sample_editable_2_length;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("100"))
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
    'Cookie': 'PHPSESSID=6be0313be3f3ddd59f1f52a348d5302a;SERVERID=2f10eec84ff44497b2cad05bed41e04a|1682826972|1682826892; PHPSESSID=6be0313be3f3ddd59f1f52a348d5302a; SERVERID=2f10eec84ff44497b2cad05bed41e04a|1682913055|1682913055',
    'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
    'Accept': '*/*',
    'Host': 'ht.srtt.nctian.com',
    'Connection': 'keep-alive',
    'Referer': 'http://ht.srtt.nctian.com/ctrl/resource',
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/ctrl/resource", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

# def getHtmlList(url):
#     try:
#         headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                         'Chrome/51.0.2704.63 Safari/537.36'}
#         r = requests.get(url, headers = headers, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.textpip
#     except:
#         print("1")

      
if __name__ == '__main__':
    conn = http.client.HTTPSConnection("ht.srtt.nctian.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=action;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("批量通过"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=opers;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("ad_lnsh"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=record[];'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("3070184"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=sample_editable_2_length;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("100"))
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
    'Cookie': 'PHPSESSID=6be0313be3f3ddd59f1f52a348d5302a;SERVERID=2f10eec84ff44497b2cad05bed41e04a|1682826972|1682826892; PHPSESSID=6be0313be3f3ddd59f1f52a348d5302a; SERVERID=2f10eec84ff44497b2cad05bed41e04a|1682913055|1682913055',
    'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
    'Accept': '*/*',
    'Host': 'ht.srtt.nctian.com',
    'Connection': 'keep-alive',
    'Referer': 'http://ht.srtt.nctian.com/ctrl/resource',
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }

    print(headers)
    print(payload)



    # conn.request("POST", "/ctrl/resource", payload, headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))