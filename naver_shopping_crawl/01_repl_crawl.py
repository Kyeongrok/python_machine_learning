# until 나까지 나누어서 나머지가 0이 아닌동안
import requests
import json

def get_repl(merchantNo, originProductNo, pageNo):

    itemsPerPage = '30'
    url = f'https://smartstore.naver.com/i/v1/reviews/paged-reviews?page={str(pageNo)}&pageSize={itemsPerPage}&merchantNo=500071344&originProductNo=280423930&sortType=REVIEW_CREATE_DATE_DESC'
    print(url)
    data = requests.get(url)

    jo = json.loads(data.content)
    print(jo)

merchantNo = '500071344'
originProductNo = '500071344'

get_repl(merchantNo, originProductNo, 1)
