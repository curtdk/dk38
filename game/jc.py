from multiprocessing import Process
from threading import Thread
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

def demo1(N):
    flag = True
    for i in range(N):
        flag = not flag
    print('end')

def test1(N):
    print("Single thread")
    demo1(N)
    demo1(N)

def test2(N):
    print("Two thread with Python threading library")
    thread1 = Thread(target=demo1, args=(N,))
    thread2 = Thread(target=demo1, args=(N,))
    thread1.start()
    thread2.start()
    # thread1.join()
    # thread2.join()

def test3(N):
    print("Two process")
    p1 = Process(target=demo1, args=(N,))
    p2 = Process(target=demo1, args=(N,))
    # p3 = Process(target=demo1, args=(N,))
    # p4 = Process(target=demo1, args=(N,))
    # p5 = Process(target=demo1, args=(N,))
    # p6 = Process(target=demo1, args=(N,))
    p1.start()
    p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
 



if __name__ == '__main__':
    # test1(int(1e9))
    # test2(int(1e9))
    # test3(int(1e9))
    game1(1)