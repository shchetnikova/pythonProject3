#1

import http.client
import json
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/3',)
r1 = conn.getresponse().read().decode()
r1_json = json.loads(r1)
print(r1_json['number'])

#2

conn.request('GET', '/number/?option=3',)
r2 = conn.getresponse().read().decode()
r2_json = json.loads(r2)
print(r2)
result = r1_json['number'] * r2_json['number']
print(result)

#3

headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/number/', 'option=3', headers)
r3 = conn.getresponse().read().decode()
r3_json = json.loads(r3)
print(r3)
result2 = r3_json['number'] - r2_json['number']
print(result2)

#4

headers = {'Content-type': 'application/json'}
conn.request('PUT', '/number/', '{"option":3}', headers)
r4 = conn.getresponse().read().decode()
r4_json = json.loads(r4)
print(r4_json)
result3 = r4_json['number']//r3_json['number']
print(result3)

#5

conn.request('DELETE', '/number/', '{"option":3}',)
r5 = conn.getresponse().read().decode()
r5_json = json.loads(r5)
print(r5_json)
result4 = r5_json['number'] + r4_json['number']
print(result4)