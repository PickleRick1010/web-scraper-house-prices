from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
                 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content

soup = BeautifulSoup(c,"html.parser")

find = soup.find_all("div",{"class":"property-card"})

list1 = []

for item in find:
    
    d = {}
    
    d["Price"] = item.find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")
    
    d["Address"] = item.find("div",{"class":"property-address"}).text.replace("\n","").replace(" ","")
     
    d["Locality"] = item.find("div",{"class":"property-city"}).text.replace("\n","").replace(" ","")
    
    try:
        d["Beds"] = item.find("div",{"class":"property-beds"}).find("strong").text.replace("\n","").replace(" ","")
    except:
        d["Beds"] = None
    
    try:
        d["Area"] = item.find("div",{"class":"property-sqft"}).find("strong").text.replace("\n","").replace(" ","")
    except:
        d["Area"] = None
    
    try:
        d["Baths"] = item.find("div",{"class":"property-baths"}).find("strong").text.replace("\n","").replace(" ","")
    except:
        d["Baths"] = None
    
    try:
        d["Half Baths"] = item.find("div",{"class":"property-half-baths"}).find("strong").text.replace("\n","").replace(" ","")
    except:
        d["Half Baths"] = None    
        
    list1.append(d)
    
df = pd.DataFrame(list1)
# df.to_csv("UDEMY Python/App-7/webscrape.csv") TO SAVE IN CSV FORMAT