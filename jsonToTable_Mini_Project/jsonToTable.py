import requests
import json
import time
import sqlite3

from configparser import ConfigParser

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
    
    dbLoc = config_object["DATABASES"]    
    activeUsersLoc = dbLoc["ACTIVEUSERS"]

    urls = config_object["URLS"]    
    usaUrl = urls["USAAPI"]

    conn = sqlite3.connect(activeUsersLoc)
    c = conn.cursor()

    c.execute('''
            CREATE TABLE IF NOT EXISTS activeUsers
            (   [metric_taken_at] TEXT,
                [active_users] INTEGER )
            ''')
                        
    conn.commit()

    
    print("\n\nA Job Cycle has been initialized")
    while True:
        statusBool = False
        for i in range(5):
            if isOnServer(usaUrl):
                print("API availabe...")
                r = requests.get(usaUrl).text
                statusBool = True
                break
            else:
                print("API not available... retrying...")
                statusBool = False
        if(statusBool == False):
            print("Waiting 5 minutes to check again...")
            time.sleep(5*60)
            continue
        else:
            print("\n\nData Gathering (API) started...")

            data = json.loads(r)
            active = int(data['data'][0]['active_visitors'])
            date = data["taken_at"]

            c.execute(f''' INSERT INTO activeUsers (metric_taken_at, active_users)
                           VALUES ('{date}',{active})
                    ''')
            conn.commit()
            print("\n\nWaiting 5 minutes to check again...")
            time.sleep(5*60)
 