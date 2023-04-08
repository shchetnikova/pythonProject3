
import http.client
import json
def operate(data: str, left: int):
    dict = json.loads(data)
    if dict['operation'] == 'mul':
        return left * dict['number']
    if dict['operation'] == 'sub':
        return left - dict['number']
    if dict['operation'] == 'div':
        return left / dict['number']
    if dict['operation'] == 'sum':
        return left + dict['number']

#1

connect = http.client.HTTPConnection("167.172.172.227:8000")
connect.request ("GET", "/number/3")
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = json.loads(decoded_body)['number']
print(left)

#2

connect = http.client.HTTPConnection("167.172.172.227:8000")
connect.request('GET', '/number/?option=3')
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = int(operate(decoded_body, left))
print(left)

#3

connect = http.client.HTTPConnection("167.172.172.227:8000")
headers = {'Content-type': 'application/x-www-form-urlencoded'}
connect.request('POST', '/number/', 'option=3', headers)
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = int(operate(decoded_body, left))
print(left)

#4

connect = http.client.HTTPConnection("167.172.172.227:8000")
headers = {'Content-type': 'application/json'}
connect.request('PUT', '/number/', json.dumps({'option': 3}), headers)
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = int(operate(decoded_body, left))
print(left)

#5

connect = http.client.HTTPConnection("167.172.172.227:8000")
connect.request('DELETE', '/number/', json.dumps({'option': 3}))
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = int(operate(decoded_body, left))
print(left)