import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class NoArgumentError(Exception):
	pass

class InvalidArgumentError(Exception):
	pass

try:
	query = sys.argv[1].strip()
	if query=='':
		raise InvalidArgumentError('Type something proper for searching!')
	driver = webdriver.Firefox()
	driver.get('https://www.google.co.in')
	WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'q')))
	g_search_box = driver.find_element_by_name('q')
	g_search_box.send_keys('Wikipedia\n')
	WebDriverWait(driver,20).until(EC.presence_of_element_located((By.LINK_TEXT,'Wikipedia, the free encyclopedia')))
	wiki_link = driver.find_element_by_link_text('Wikipedia, the free encyclopedia')
	wiki_link.click()
	WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'search')))
	w_search_box = driver.find_element_by_name('search')
	w_search_box.send_keys(query+'\n')
except IndexError:
	raise NoArgumentError('Type in something to search!')


