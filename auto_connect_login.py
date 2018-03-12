from subprocess import check_output,Popen,STDOUT,PIPE
from selenium import webdriver


wifi_ssid='VesCampus'
wifi_password=''.encode('utf-8')
login_username=''
login_password=''
login_url='http://veswifi.com/login'

handle=Popen('netsh wlan connect ' + wifi_ssid,shell=True,stdout=PIPE,stderr=STDOUT,stdin=PIPE)

if handle:
	handle.stdin.write(wifi_password)
	browser=webdriver.Chrome()
	response=browser.get(login_url)
	username=response.find_element_by_id('username')
	username.send_keys(login_username)
	password=response.find_element_by_id('password')
	password.send_keys(login_password)
	login_button=response.find_element_by_id('login')
	login_button.click()

'''while handle.poll()==None:
	print(handle.stdout.readline().strip())'''

	#print('valar morghulis')