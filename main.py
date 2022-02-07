import requests
import json
import os

TOKEN = 'your token'

def shortener():
        #getting long url
        long_url = input('Your long URL:')
        #doing get request to cutt.ly
        response = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(TOKEN, long_url))
        #getting json string and extract shrort url
        short_link = json.loads(response.text)['url']['shortLink']
        #auto copy
        os.system('echo ' + short_link.strip() + '| clip')
        #print short url
        print(short_link)    

if __name__ == '__main__':
        shortener()