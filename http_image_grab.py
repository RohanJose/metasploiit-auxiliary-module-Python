
#!/usr/bin/env python3
from metasploit import module
from bs4 import BeautifulSoup
import requests

metadata = {
    'name': 'ImageScraper',
    'description': 'Python Image Scraper Module for Metasploit',
    'authors': ['Rohan Jose'],
    'date': '2024-02-14',
    'license': 'MSF_LICENSE',
    'type': 'auxiliary',
    'options': {
        'URL': {
            'type': 'string',
            'description': 'Target URL',
            'required': True
        }
    }
}

def run(args):
    url = args['URL']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        module.log(image['src'])

if __name__ == '__main__':
    module.run(metadata, run)
