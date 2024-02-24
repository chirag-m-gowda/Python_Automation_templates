# Python program template to automate sending Instagram messages to multiple users.
# Before running this program, make sure that Two-Factor authentication for instagram login is turned off.
""" python package required: Selenium (pip install selenium), 
webdriver-manager(pip install webdriver-manager),chrome driver(automatic download and install in code), 
google chrome browser """

# importing modules
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install()) #download and installation of chrome driver

# enter receiver user names:
user = ['user_name1', 'user_name2'] # enter instagram username of the recipient.
message_ = ("Type your message here") #enter the message you want to send.


class bot:
	def __init__(self, username, password, user, message):
		self.username = username
		self.password = password
		self.user = user
		self.message = message
		self.base_url = 'https://www.instagram.com/'
		self.bot = driver
		self.login()

	def login(self):
		self.bot.get(self.base_url)

		enter_username = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'username')))
		enter_username.send_keys(self.username)
		enter_password = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'password')))
		enter_password.send_keys(self.password)
		enter_password.send_keys(Keys.RETURN)
		time.sleep(5)

		# XPath of any element can be found by inspecting the html code of the element >> right click on the html code >> copy >> copy XPath.

		# Bypass-first pop-up(save your login info pop-up):
		self.bot.find_element(By.XPATH,'Copy paste XPath of Not now button in first pop-up here ').click()
		time.sleep(5)

		# Bypass-2nd pop-up (Turn on notifications pop-up):
		self.bot.find_element(By.XPATH,'Copy paste XPath of Not now button in second pop-up here').click()
		time.sleep(5)

		# clicks on the message direct button:
		self.bot.find_element(By.XPATH,'Copy paste XPath of messages button here').click()
		time.sleep(3)

		# clicks on pencil icon:
		self.bot.find_element(By.XPATH,'Copy paste XPath of pencil icon here').click()
		time.sleep(2)
		for i in user:

			# enter the username (Put Xpath of username search field here:)
			self.bot.find_element(By.XPATH,'Copy paste Xpath of username search field here').send_keys(i)
			time.sleep(3)

			# click on the username (Put XPath of clicking on the username found after search here:)
			self.bot.find_element(By.XPATH,'Copy paste XPath of clicking on the username found after search here:').click()
			time.sleep(4)

			# next button
			self.bot.find_element(By.XPATH,'Copy paste XPath of next button here').click()
			time.sleep(4)

			# click on message area
			send = self.bot.find_element(By.XPATH,'Copy paste XPath of clicking on message area here:').click()

			# types message
			send.send_keys(self.message)
			time.sleep(1)

			# send message
			send.send_keys(Keys.RETURN)
			time.sleep(2)

			# clicks on direct option or pencil icon
			self.bot.find_element(By.XPATH,'Copy paste XPath of Pencil icon here').click()
			time.sleep(4)


def init():
	bot('login_id here', 'Password here', user, message_) # Put your instagram login credentials here.

	# When the program ends, it will show "Messages sent" in the terminal.
	input("Messages sent")


# Calling the function.
init()
