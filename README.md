# SkyPro / Homework 24

Web server on Flask with typing and annotation of all methods and queries validation with marshmallow, which:
1) "Repeats" the functionality of the Linux command line for processing files.
2) Сonsists of one POST method. The method meets the following requirements:
   * Available on the path "/perform_query"
   * It takes a dict with queries (cmd + value), where there should be from one to several queries, and a file_name parameter with the path to the data file.
   * Commands available for execution: 
      - "filter": "text", 
      - "map": "integer",
      - "sort": "asc/desc"
      - "unique": "",
      - "limit": "integer"
      - "regex": "regular expression string"
   ```
   # Server request example
   
   import requests
   
   url = "http://127.0.0.1:5000/perform_query"
   
   payload = {
      'queries': [
        {
            'cmd': 'filter',
            'value': 'GET'
        },
        {
            'cmd': 'regex',
            'value': 'images/\\w+\\.png'
        },
        {
            'cmd': 'unique',
            'value': ''
        },
        {
            'cmd': 'sort',
            'value': ''
        }
        ],
      'file_name': 'apache_logs.txt',
   }

    response = requests.request("POST", url, data=payload)
    print(response.text)
   ```
   * The method looks for files inside the data directory. The data folder is in the same folder as the web server.
   * Process the file following the written request and returns the response to the client

## Usage

Run "app.py".