# until 나까지 나누어서 나머지가 0이 아닌동안
import requests
import json

def get_repl(merchantNo, originProductNo, pageNo):

    itemsPerPage = '30'
    # url = f'https://smartstore.naver.com/i/v1/reviews/paged-reviews?page={str(pageNo)}&pageSize={itemsPerPage}&merchantNo={merchantNo}&originProductNo={originProductNo}&sortType=REVIEW_CREATE_DATE_DESC'
    url = f'https://smartstore.naver.com/i/v1/reviews/paged-reviews?page={str(pageNo)}&pageSize=30&merchantNo=500071344&originProductNo=280423930&sortType=REVIEW_CREATE_DATE_DESC'
    print(url)
    data = requests.get(url)

    s = data.content
    print(s)
    jo = json.loads(s)
    return jo


def save(page_no):
    merchantNo = '500071344'
    originProductNo = '500071344'

    jo = get_repl(merchantNo, originProductNo, page_no)

    with open(f'result/{page_no}.json', 'w+') as f:
        f.write(json.dumps(jo))

for i in range(1666, 1693):
    save(i)