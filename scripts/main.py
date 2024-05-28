import requests
import os
from tqdm import tqdm

from bs4 import BeautifulSoup as bs

output_dir = 'articles/'

if __name__ == '__main__':
    with open('links.txt', 'r') as file:
        links = file.readlines()
        for cnt, url in enumerate(tqdm(links)):
            try:
                url = url.strip()
                response = requests.get(url)
                soup = bs(response.text, 'html.parser')
                article = soup.find(id="main-pagecontent__div")
                
                result = ''
                for paragraph in article.find_all('p'):
                    result += paragraph.get_text()

                output_file = f'{output_dir}/article_{cnt}.txt'
                with open(output_file, 'w') as file:
                    file.write(result)
            except Exception as e:
                print(f'Error: {e}')
                continue
