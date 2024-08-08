from bs4 import BeautifulSoup
import requests
import time

def get_info():
  html_text = requests.get('https://en.wikipedia.org/wiki/Cat').text
  soup = BeautifulSoup(html_text, 'lxml')
  cats = soup.find_all('div', class_ = 'mw-content-ltr mw-parser-output')
  for cat in cats:
    heading3 = cat.find_all('div', class_ = 'mw-heading mw-heading3')
    for index, h3 in enumerate(heading3):
      sub_heading = h3.find('h3').text
      with open(f'posts/{index}.txt', "w") as f:
        f.write(f'Sub-heading: {sub_heading.strip()} \n')
      print(f"File saved: {index}")


if __name__ == '__main__':
  while True:
    get_info()
    time_wait = 10
    print(f"Waiting {time_wait} seconds...")
    time.sleep(time_wait * 60)