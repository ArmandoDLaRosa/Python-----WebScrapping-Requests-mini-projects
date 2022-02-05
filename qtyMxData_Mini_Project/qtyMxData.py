import requests
import time
import re
from bs4 import BeautifulSoup
from configparser import ConfigParser
from collections import Counter

def isOnServer(url):
    # This function follows an Binary approach, either the request suceeded or failed
    try:
        result = requests.get(url)
        return result.ok  #Ok or 200 means the request suceeded
    except requests.exceptions.RequestException as e:  
        return False # If you ever decide to manage connection errors by type - https://stackoverflow.com/a/16511493

if __name__ == '__main__':

    #Read .ini file
    config_object = ConfigParser(interpolation=None)
    config_object.read("/home/armando/Github Repos/WebScrapping-exercises/config.ini")
    
    siteUrls = config_object["URLS"]    
    datosUrl = siteUrls["DATOSMX"]
    apiUrl = siteUrls["APIDATOSMX"]

    print("\n\nA Job Cycle has been initialized")
    while True:
        statusBool = False
        for i in range(5):
            if isOnServer(datosUrl) & isOnServer(apiUrl):
                print("Webpage and API availabe...")
                html = requests.get(datosUrl).text 
                r = requests.get(apiUrl).text
                statusBool = True
                break
            else:
                time.sleep(5)
                print("Webpage or API not available... retrying...")
                statusBool = False
        if(statusBool == False):
            print("Waiting 10 minutes to check again...")
            time.sleep(10*60)
            continue
        else:
            print("\n\nData Gathering (API) started...")

            lista = re.findall('"format":"(.*?)","', r)
            print("\nAccording to the Datos MX's API the total of datasets is: ",  len(lista), "\n by file type", Counter(lista),)

            time.sleep(5)
            print("\n\nData Gathering (WebScrapping) started...")
            soup = BeautifulSoup(html, 'lxml')
            qty = soup.find('div',  class_="col-md-7 col-sm-7 results-home").p.text

            print('According to webscrapped data, the total of data items is:', re.findall('[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', qty)[0].replace(".",","))
            print("\n\nWaiting 10 minutes to check again...")
            time.sleep(10*60)
 


