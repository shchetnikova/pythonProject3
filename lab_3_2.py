#2

conn.request('GET', '/number/?option=3',)

r2 = conn.getresponse().read().decode()

r2_json = json.loads(r2)

print(r2)

result = r1_json['number'] * r2_json['number']

print(result)