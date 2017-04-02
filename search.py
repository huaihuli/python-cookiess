import requests,pickle

session = requests.Session()
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}
session.headers = header
with open('cookie.txt','rb') as f:
    cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
    session.cookies = cookies
try:
    result = session.get('https://www.douban.com/people/156542526/')
    if result.status_code == 200:
        print(result.text)
except:
    print('error')