# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class LOGIN:
    def __init__(self, username, password, session, cookies):
        self.username = username
        self.password = password
        self.session = session
        self.cookies = cookies

    def login(self):
        s = requests.session()
        r = s.get('https://www.linkedin.com/')
        soup = BeautifulSoup(r.text, 'lxml')
        loginCsrfParam = soup.find('input', id='loginCsrfParam-login')['value']
        sourceAlias = soup.find('input', id='sourceAlias-login')['value']

        payload = {
            'session_key': self.username,
            'session_password': self.password,
            'loginCsrfParam': loginCsrfParam,
            'sourceAlias': sourceAlias
        }

        res = s.post('https://www.linkedin.com/uas/login-submit', data=payload)


user1 = LOGIN('netspman@163.com', 'wodelinkedinmima')

res = user1.session.get('http://www.linkedin.com/in/thomas7733?authType=name&authToken=cBSq&trk=miniprofile-name-link', cookies=cookie)
print res.text

