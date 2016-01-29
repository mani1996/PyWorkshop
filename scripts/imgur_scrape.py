from subprocess import call
from bs4 import BeautifulSoup
import requests,time

def main():
	url = 'http://imgur.com/gallery/UMVNg'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	div_tags = soup.findAll('div', {'class':'post-image'})
	for tag in div_tags:
		img_tag = tag.find('img')
		img_url = img_tag['src'][2::]
		call(['wget', img_url],shell=True)
		
if __name__ == '__main__':
	main()

