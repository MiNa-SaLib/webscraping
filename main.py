import requests
import bs4
import csv
from itertools import zip_longest

eposid=[]
dayOfEposid=[]
page = requests.get("https://to.akwam.cz/series/3711/%D8%A7%D9%84%D8%BA%D8%B1%D9%81%D8%A9-207")
htmlcode=page.content
#print(htmlcode)
soup = bs4.BeautifulSoup(htmlcode, "html.parser")
ep=soup.find_all("h2",{"class":"font-size-18 text-white mb-2"})
for i in range(len(ep)):
    eposid.append(ep[i].text)
date=soup.find_all("p",{"class":"entry-date font-size-12 text-muted mb-2"})
for i in range(len(date)):
    dayOfEposid.append(date[i].text)
#if i want to print data in the console
for i in range(len(eposid)):
    print(f"{eposid[i]} {dayOfEposid[i]}")

'''
#if i want to print data in csv file
allthing=[eposid ,d]
all=zip_longest(*allthing)
with open("D:\mina salib.csv","w") as file:
    writer=csv.writer(file)
    writer.writerow(["Eposid","Date of Publishing"])
    writer.writerows(all)
'''
