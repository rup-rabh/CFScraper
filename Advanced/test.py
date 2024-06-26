import json
import seleTut as scrape

with open('links.json','r') as file:
    links = json.load(file)
    
for key in links:
    print(links[key])
    scrape.extract(links[key])
    # if(int(key)>=2):
    #     break