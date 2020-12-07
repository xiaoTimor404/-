import requests

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
for i in range(1,15):
    data = {
        'on': 'true',
        'page': str(i),
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }

    response = requests.post(url=url, headers=headers, data=data)

    page_list_json = response.json()

    id_list = page_list_json['list']

    for id_id in id_list: 
        xiangqing_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
        data = {'id' : str(id_id['ID'])}
        response = requests.post(url=xiangqing_url, headers=headers, data=data)
        xiangqing = response.json()
        print('企业名称：'+ xiangqing['epsName'])
        print('许可证编号：'+ xiangqing['productSn'])