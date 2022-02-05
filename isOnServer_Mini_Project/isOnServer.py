# This could be turn into a small API that serves a simple frontend

import requests
import regex
import time
from configparser import ConfigParser
from datetime import datetime
import pytz

def isUrlValid(urlString):
    #Read .ini file
    # None - Avoids that '%' throws an error, as '%' works both in .ini and patter as a character
    config_object = ConfigParser(interpolation=None)
    config_object.read("/home/armando/Github Repos/WebScrapping-exercises/config.ini") #Path
    patternInfo = config_object["PATTERNS"]

    # Get a match that follows the right URL pattern from the input string
    # are the match and input  equal? then URL is valid
    return True if regex.search(f'{patternInfo["URLPATTERN"]}', urlString) else False

def isOnServer(url):
    # This function follows an Binary approach, either the request suceeded or failed
    try:
        result = requests.get(url)
        return result.ok  #Ok or 200 means the request suceeded
    except requests.exceptions.RequestException as e:  
        return False # If you ever decide to manage connection errors by type - https://stackoverflow.com/a/16511493

def urlDebugger(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        return SystemExit(e)

def logger(statusBool, url=''):

    dateTimeStr = datetime.now(pytz.timezone('America/Mexico_City') ).strftime("%d/%m/%Y %H:%M:%S")
    file_object = open('logs.txt', 'a')
    file_object.write("\n\n\nURL: " + url + "\nDate: " + dateTimeStr + '\n')
    
    if statusBool == True: # The try succeded
        responseStr = "Status: Active"
        print(responseStr)
        file_object.write(responseStr)
        file_object.close()
    else:
        responseStr = "Status: Inactive \n" + "Error: " + str(urlDebugger(urlString))
        print(responseStr)
        file_object.write(responseStr)
        file_object.close()

if __name__ == '__main__':
        # URL input
        print("Job 'isOnServer' started ... \n")

        urlString = input("Write your URL including the 'http://'  \nExample- http://example.com \nYour URL: ")
        if not (isUrlValid(urlString)) :
            while True:
                urlString = input("\nInvalid URL - Follow the example and don't forget the 'http://'  \nExample- http://example.com \nYour URL: ")
        
                # URL validation according to htttp URL patterns
                if isUrlValid(urlString) :
                    break     
        
        # Job Cycling to verify the status
        print(f"\nThe status of {urlString} will be verified every 10 minutes")
        file_object = open('logs.txt', 'a')
        file_object.write("\n\nJob Initialized______ " + urlString + "")
        file_object.close()
        while True:
            # Active - Url is on the server / Inactive - URL had some error
            logger(True, urlString) if isOnServer(urlString) else logger(False, urlString)
            print("\nWaiting 10 minutes to check again... \nRemember the logs.txt file stores a history of each cycle result")
            time.sleep(10*60) # function works in seconds