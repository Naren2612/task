import requests


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
    'type': '1',
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
total_pages = js.get('maxPageNum')
result = js['rows']
for details in result:
    name = details.get('name')
    industry = details.get('IndustryName')
    region = details.get('areaName')
    source = details.get('capitalSourceName')
    date = details.get('createTime')
    detail_url = "http://en.chinabidding.mofcom.gov.cn/bidDetail" + details.get('filePath')

    data = {
        "NAME" : name,
        "INDUSTRY" : industry,
        "REGION" : region,
        "SOURCE" : source,
        "PUBLISH DATE" : date,
        "DETAIL URL": detail_url
    }
    print(data)
    
