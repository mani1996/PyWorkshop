import requests
from bs4 import BeautifulSoup
from config import WEBMAIL_ID, PASSWORD

def login():
    my_session = requests.session()
    response = my_session.get('http://mess.nitt.edu/login')
    soup = BeautifulSoup(response.text, 'html.parser')
    token_tag = soup.find('input', {'name': '_token'})
    token = token_tag['value']
    print 'CSRF Token = ' + token
    login_dict = {'webmail_id': WEBMAIL_ID,
        'password': PASSWORD,
        '_token': token}
    login_response = my_session.post('http://mess.nitt.edu/auth/login', data=login_dict)
    soup = BeautifulSoup(login_response.text, 'html.parser')
    login_text = soup.find('div', {'class':'row'})
    print login_text.text
    
if __name__ == '__main__':
    login()