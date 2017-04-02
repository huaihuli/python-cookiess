import requests ,pickle
import re


class creat_cokies():
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }

    post_data={
        'source': 'None',
        'remember': 'on',
        'redir': 'https://www.douban.com',
        'login': '登录',
        'form_password': 'WangNing7411.',
        'form_email': '18292811977',
        'captcha-solution': '',
        'captcha-id': '',
    }

    session = requests.Session()
    session.headers = header

    def get_index(self):
        try:
            index = self.session.get('https://www.douban.com/accounts/login', timeout=15)
            if index.status_code == 200:
                return index.text
        except:
            print('请求主页出错！')

    def prase_index(self,html):
        pattern = re.compile(r'<img id="captcha_image" src="(.*?)" alt="captcha"')
        pattern2 = re.compile(r'<input type="hidden" name="captcha-id" value="(.*?)"/>')
        yanzheng= pattern.findall(html)
        key = pattern2.findall(html)
        src_img = yanzheng[0]
        self.post_data['captcha-id'] = key[0]
        try:
            result =self.session.get(url=src_img,timeout=15)
            if result.status_code ==200:
                with open('img.jpg','wb') as img:
                    img.write(result.content)
                captcha_solution = input('验证码已保存，请输入:')
                self.post_data['captcha-solution'] = captcha_solution
        except:
            print('请求验证码出错:')

    def login_douban(self):
        try:
            result = self.session.post(url='https://accounts.douban.com/login',data=self.post_data)
            if result.status_code ==200:
                with open('cookie.txt', 'wb') as f:  # 保存cookies
                    pickle.dump(requests.utils.dict_from_cookiejar(self.session.cookies), f)
        except:
            print('登陆出错')


    def __init__(self):
        html = self.get_index()
        self.prase_index(html)
        self.login_douban()

creat_cokies()