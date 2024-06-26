from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
url = 'https://codeforces.com/problemset/problem/1935/D'
def extract(link):
    # link = input()


    service = Service(executable_path="chromedriver.exe") 

    driver = webdriver.Chrome(service=service)

    driver.get(link)
    #created json file
    jsonFile = {}
    #accessing problem div
    allMain = driver.find_elements(By.CSS_SELECTOR,".problem-statement > div")
    #Header infos
    problem_head = allMain[0]
    #accessing last children of header
    head_children = problem_head.find_elements(By.XPATH,'./child::*')

    headDict = {}
    #last element of every children were useful strings
    for el in head_children:
        headDict[el.get_attribute('class')] = driver.execute_script('return arguments[0].lastChild.data;',el)
    jsonFile["header"] = headDict
    #problem statement
    problem_statement = allMain[1].text.splitlines()
    problem_statement =' '.join(problem_statement) 
    jsonFile['problemStatement'] = problem_statement
    #Rest of elements
    for div in range(2,len(allMain)):
        name = allMain[div].find_element(By.CLASS_NAME,'section-title').text
        texts = allMain[div].text.splitlines()
        texts = ' '.join(texts)
        jsonFile[name.lower()] = texts
    #####################Side-bar Quest
    #tags
    tags = driver.find_elements(By.CLASS_NAME,"tag-box")
    jsonFile['tags'] = []
    for tag in tags:
        jsonFile['tags'].append(tag.text)
    #round
    round = driver.find_element(By.ID,'sidebar').find_element(By.TAG_NAME,'a').text
    jsonFile['round'] = round
    ###############detailed Scraping ######################
    jsonFile = json.dumps(jsonFile, indent=4)

    with open("data.json", 'w') as f:
        json.dump(jsonFile, f)
    
    #########for chain scraping of tags ###################
    # data =[]
    # with open("tagAn.json", 'r') as f:
    #     data = json.load(f)
    # newData = jsonFile['tags']
    # data.append(newData);
    # # print(data)
    # with open("tagAn.json", 'w') as f:
    #     json.dump(data,f,indent=4)
    #OverNOut
    driver.quit()
    
    
extract(url)