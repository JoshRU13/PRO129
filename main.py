import csv
data=[]
with open("dataset1.csv","r")as f:
    r1=csv.reader(f)
    for i in r1:
        data.append(i)
headers=data[0]
planet_data=data[1:]
for i in planet_data:
    i[2]=i[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("dataset2.csv","a+")as f:
    r1=csv.writer(f)
    r1.writerow(headers)
    r1.writerows(planet_data)