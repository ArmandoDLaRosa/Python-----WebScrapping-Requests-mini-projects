import sqlite3
from sqlite3 import Error
from configparser import ConfigParser

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    config_object = ConfigParser(interpolation=None)
    config_object.read("/home/armando/Github Repos/WebScrapping-exercises/config.ini")
        
    dbLoc = config_object["DATABASES"]    
    activeUsersLoc = dbLoc["ACTIVEUSERS"]
    create_connection(activeUsersLoc)