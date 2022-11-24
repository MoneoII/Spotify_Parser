import json


f =open('StreamingHistory0.json')
data = json.load(f)

a=0
nameL=[]

for i in range(len(data)):
	nameL.append((data[i]['trackName']))
dicL=dict.fromkeys(nameL)

for i in dicL:
	dicL[i]=0

for i in nameL:
	dicL[i]=dicL[i]+1

for i in dicL:
	a=a+dicL[i]
print(data)