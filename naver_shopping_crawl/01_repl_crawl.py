# until 나까지 나누어서 나머지가 0이 아닌동안
import requests

url = f'https://smartstore.naver.com/i/v1/reviews/paged-reviews?page=&{1}pageSize=20&merchantNo=500071344&originProductNo=280423930&sortType=REVIEW_CREATE_DATE_DESC'
data = requests.get(url)
print(data.content)