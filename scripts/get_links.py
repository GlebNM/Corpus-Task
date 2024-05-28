import requests

from bs4 import BeautifulSoup as bs
prefix = 'https://www.ixbt.com'
url = 'https://www.ixbt.com/articles/'
if __name__ == '__main__':
    for year in [2020, 2021, 2022, 2023]:
        for month in range(1, 13):
            url = f'https://www.ixbt.com/articles/{year}/{month}/'
            response = requests.get(url)
            soup = bs(response.text, 'html.parser')
            # print(soup.prettify())
            # extract text from the article
            article_links = soup.find_all('a', class_="item__text--title")
            
            for link in article_links:
                print(prefix + link['href'])
    
    for month in range(1, 6):
        url = f'https://www.ixbt.com/articles/2024/{month}/'
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        # print(soup.prettify())
        # extract text from the article
        article_links = soup.find_all('a', class_="item__text--title")
        
        for link in article_links:
            print(prefix + link['href'])
