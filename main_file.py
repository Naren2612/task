import requests
import pandas as pd


cookies = {
    'insert_cookie': '67183482',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'http://en.chinabidding.mofcom.gov.cn',
    'Connection': 'keep-alive',
    'Referer': 'http://en.chinabidding.mofcom.gov.cn/channel/EnSearchList.shtml?tenders=1',
    # 'Cookie': 'insert_cookie=67183482',
}
data = {
    'pageNumber': '1',
    'pageSize': '10',
    'type': '',
    'industry': '',
    'provinceCode': '',
    'keyword': '',
    'capitalSourceCode': '',
}

count = 0
tenders_data = []



def crawl_total_pages():
    response = requests.post(
        'http://en.chinabidding.mofcom.gov.cn/zbwcms/front/en/bidding/bulletinList',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    js = response.json()
    total_pages = js.get('maxPageNum')
    return total_pages

def crawl_detail(js):
    result = js['rows']
    for details in result:
        name = details.get('name')
        industry = details.get('industryName')
        region = details.get('areaName')
        source = details.get('capitalSourceName')
        date = details.get('createTime')
        detail_url = "http://en.chinabidding.mofcom.gov.cn/bidDetail" + details.get('filePath')
        ten_data = {
            "NAME" : name,
            "INDUSTRY" : industry,
            "REGION" : region,
            "SOURCE" : source,
            "PUBLISH DATE" : date,
            "DETAIL URL": detail_url
            }
        print(ten_data)
        tenders_data.append(ten_data)

def request_json(total_pages,count):
    for pagenumber in range(1,total_pages):
        data = {
        'pageNumber': pagenumber,
        'pageSize': '10',
        'type': '',
        'industry': '',
        'provinceCode': '',
        'keyword': '',
        'capitalSourceCode': '',
        }
        response = requests.post(
        'http://en.chinabidding.mofcom.gov.cn/zbwcms/front/en/bidding/bulletinList',
        cookies=cookies,
        headers=headers,
        data=data,
        )
        js = response.json()
        count += 1
        print(count)
        crawl_detail(js)


total_pages = crawl_total_pages()
request_json(total_pages,count)
df = pd.DataFrame(tenders_data)
df.to_csv('tenders data.csv', index=False)

