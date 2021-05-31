import os, sys, time, json, urllib3, requests, multiprocessing
urllib3.disable_warnings()
import time
import numpy as np
import pandas as pd
import argparse

delay=0.5
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--place", required=True,help="enter the place name")
ap.add_argument("-o", "--output_file", required=True,help="enter the outfile name")
args = vars(ap.parse_args())

def Downloading(query_url,file_path):
	print("initializing download")
	time.sleep(delay)
	main_response = requests.get(url=query_url, verify=False)
	print("getting data from API !")
	json_response = json.loads(main_response.text)
	time.sleep(delay)
	print("Saving data")
	df = pd.DataFrame.from_dict(json_response['features'][0]['properties']['parameter'])
	return df,file_path
	#df.to_csv(file_path)

query_url = 'https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&identifier=SinglePoint&tempAverage=INTERANNUAL&parameters=T2M,RH2M&startDate=2000&endDate=2020&lat={latitude}&lon={longitude}&outputList=JSON&userCommunity=SSE'
file_path = "{outfile}_{place}_File_Lat_{latitude}_Lon_{longitude}.csv"

option=args["place"]
print("selected place: "+option)
time.sleep(delay)
print("coordinates initializing")

if option=="chintamani" or option=="cht":
	Latitude_Longitude = [(13.4030, 78.0395, 0)]
	place = "chintamani"
elif option=="chikkaballapur" or option=="chk":
	Latitude_Longitude = [(13.4259, 77.7697, 0)]
	place = "Chikkaballapur"
elif option=="kolar" or option =="klr":
	Latitude_Longitude = [(13.1582, 78.1258, 0)]
	place = "kolar"
elif option=="bagealli" or option=="bgl":
	Latitude_Longitude = [(13.7776, 77.8114, 0)]
	place = "bagealli"
elif option=="gowribidanur" or option=="gbn":
	Latitude_Longitude = [(13.5944, 77.5287, 0)]
	place = "gowribidanur"
time.sleep(delay)

print("loading co-ordinates")
time.sleep(delay)
Points = []
for Latitude, Longitude, Index in Latitude_Longitude:
	each_query_url = query_url.format(longitude=Longitude, latitude=Latitude)
	each_file_path = file_path.format(outfile=args["output_file"],place=place,longitude=Longitude, latitude=Latitude)
	print(Latitude,Longitude)

df2,filepath = Downloading(each_query_url, each_file_path)

df2['year'] = df2.index

first_column = df2.pop('year')
df2.insert(0, 'year', first_column)

res= pd.DataFrame(0, index=np.arange(df2.shape[0]), columns=['year', 'month','RH2M','T2M','THI'], dtype='object')

print("sample data")
for a in df2.iterrows():
	print(a[1])
	break

def thi_calc(T,H):
	RH = H/100
	thi = (0.8*T)+(RH*(T-14.4))+46.4
	return thi

for x in range(df2.shape[0]):
	new=[]
	thi = thi_calc(df2.iloc[x][2],df2.iloc[x][1])
	new.append(df2.iloc[x][0][:-2])
	new.append(df2.iloc[x][0][-2:])
	new.append(df2.iloc[x][1])
	new.append(df2.iloc[x][2])
	new.append(round(thi, 1))
	res.loc[x]=new

print("saving data to "+filepath)
res.to_csv(filepath)
