# Webscrapping Exercises

## Tools 
---
* WSL (Ubuntu 20.04)
* Vscode (Remote Wsl, Python Extension)
* Python (requests)

## What does the project do?
---
 > isOnServer.py

  Verifies that the webpage inserted in the cmd is on the server.

  Note: This might just be a chron job that sends an email or displays
        the result in a status web page. This can also be a Web service
        to help people check if their web page is on the server.

 > qtyMxData.py

  Scraps the datosMx website or requests datosMx api to get the following data
  * Qty of datasets
  * Qty of datasets per tyoe of file

 > jsonToTable.py

  [Api used](https://analytics.usa.gov/data/live/realtime.json)

  
  Gets a json from the api and trwansforms it into a table

## Setup Documentation
---
1) Create python environment (its files should be good inside the project folder)
    ```
    sudo apt install python3-virtualenv
    virtualenv scrapEnv
    ```

2) Activate python environment in the command line
    ``` 
    source scrapEnv/bin/activate
    ``` 

3) Change in vscode the interpreter to the python inside scrapEnv/bin/python3.8 ```ctrl+shif+p > 'Python Interpreter'```
   1) This way you can run the .py with the extension RUN button with the env activated.
   2) Otherwise, you'll have to run it like `python3 fileName.py` and the env activated.

4) Create a git ignore file, for inspo look at this forked repo [.git ignore examples](https://github.com/ArmandoDLaRosa/gitignore)
    > **OPTIONAL** Create a config.ini file for the env variables.
    ```
    nano .gitignore
    ```
    Paste inside the .gitignore the example + add config.ini file's name
5) Install needed libraries for the project
6) Store the requirements in a file
    ```
    pip freeze > requirements.txt
    ```
7) Make sure that there's
   1) No need to rename variable with good names
   2) No blocks of code that could be a function
   3) Documentation to understand the code
   4) No need to use objects (data and behavior)
   5) No variables that should be in the config.ini
   6) No file that should be in the .gitignore

## Resources
[Regex patterns library](https://gist.github.com/ArmandoDLaRosa/d3d36b663bc10935e2dd38754f5cf5d5)