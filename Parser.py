import json
import pandas as pd
import requests
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io
from matplotlib import mlab

f0 =open('StreamingHistory0.json')


data = json.load(f0)
data2 = data

#fig, ax = plt.subplots(1,1)


a=0
nameL=[]

for i in range(len(data)):
	nameL.append((data[i]['artistName']))
dicL=dict.fromkeys(nameL)

def AMListened():
	global a
	for i in dicL:
		dicL[i]=0

	for i in nameL:
		dicL[i]=dicL[i]+1

	for i in dicL:
		a=a+dicL[i]

	sorted_values = sorted(dicL.values()) # Sort the values
	sorted_dict = {}

	for i in sorted_values:
	    for k in dicL.keys():
	        if dicL[k] == i:
	            sorted_dict[k] = dicL[k]

	return(sorted_dict)

def SxTime(song):
	date=[]
	artist=[]
	name=[]
	timeP=[]
	for i in range(len(data)):
		if data[i]['artistName'] == data[i]['artistName']:#song:
			date.append(data[i]['endTime'][:10])
			artist.append(data[i]['artistName'])
			name.append(data[i]['trackName'])
			timeP.append(data[i]['msPlayed'])

	#x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in date]		

	lvl={'endTime':date,'artistName':artist,'trackName':name,'msPlayed':timeP}
	df=pd.DataFrame(data=lvl)
	return(df)

def DTSet(names):
	ky=dict.fromkeys(names)
	for q in names:
		ky[q]=SxTime(str(q))['endTime'].values.tolist()
		ax.hist(ky[q], bins=365, cumulative=True, histtype='step')
q=SxTime(3)
dicTime=dict.fromkeys(q['endTime'])
for i in dicTime:
	dicTime[i]=0




for i in range(len(q)):
	b=q['endTime'][i]
	dicTime[b]=dicTime[b]+(q['msPlayed'][i]/(3.6*1000000))


cumTimeArr=[0]*364
tick=0
ls=0
for i in dicTime:
	cumTimeArr[tick]=dicTime[i]+ls
	ls=cumTimeArr[tick]
	tick=tick+1

plt.bar(list(dicTime.keys()),cumTimeArr)
plt.show()
print(cumTimeArr)
'''

#col_list = SxTime('The Strokes')['endTime'].values.tolist()
#col_list2 = SxTime('Fade In Nylon')['endTime'].values.tolist()
#print(col_list2)
#DTSet(['The Strokes','Arctic Monkeys','Radiohead','Daft Punk', 'A Beacon School', 'The Smiths', 'Phoebe Bridgers', 'Elliott Smith', 'Peach Pit', 'Beach House'])


#ax.hist(col_list2, bins=50, cumulative=True,color='Red', histtype='step')
#ax.hist(col_list, bins=365, cumulative=True,color='lightblue', histtype='step')
#ax.xaxis.set_major_locator(mdates.YearLocator())
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%y'))
ax.set_xlim([dt.date(2021, 11, 22), dt.date(2022, 11, 22)])
ax.legend(['The Strokes','Arctic Monkeys','Radiohead','Daft Punk', 'A Beacon School', 'The Smiths', 'Phoebe Bridgers', 'Elliott Smith', 'Peach Pit', 'Beach House'])
ax.grid(visible=True,axis='both')
#plt.show()

print(AMListened())

'''




