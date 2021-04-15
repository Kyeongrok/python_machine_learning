
import requests
from bs4 import BeautifulSoup

url = f'https://finance.naver.com/item/frgn.nhn?code={"000660"}&page={1}'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

data = requests.get(url, headers=headers)

bsobj = BeautifulSoup(data.content, 'html.parser')
print(bsobj)
