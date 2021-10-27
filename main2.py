import csv
dataset1=[]
dataset2=[]
with open("scrapper_2.csv","r")as f:
    r1=csv.reader(f)
    for i in r1:
        dataset1.append(i)
with open("dataset2.csv","r")as f:
    r1=csv.reader(f)
    for i in r1:
        dataset2.append(i)
h1=dataset1[0]
h2=dataset2[0]
p1=dataset1[1:]
p2=dataset2[1:]
h=h1+h2
p=[]
for index,i in enumerate(p1):
    p.append(p1[index]+p2[index])
with open("full.csv","a+")as f:
    r1=csv.writer(f)
    r1.writerow(h)
    r1.writerows(p)