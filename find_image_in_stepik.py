import json
import pickle
import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

path = './chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get('https://stepik.org/lesson/4763/step/7?unit=1065')
steps = [
    ("/html/body/div/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/"
     "div/article/div/div/div[2]/div/section/div/div[1]/div/button", 40, 'click', None, False, 0),
    ('/html/body/div/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div/article'
     '/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/button', 40, 'click', None, False, 0),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', keys.Keys.ENTER, False, 1),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', 'ssh server1.stepik-local', False, 0),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', keys.Keys.ENTER, False, 0),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', 'yes', False, 1),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', keys.Keys.ENTER, False, 0),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', 'supersecret', False, 5),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', keys.Keys.ENTER, False, 0),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', 'base64 /srv/files_on_server/stepik_team.png | less', False, 0),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', keys.Keys.ENTER, False, 0),
    ('/html/body/div[2]/div[3]', 40, 'send_keys', keys.Keys.SPACE, True, 0),
]
strings = []

for xpath, timeout, action, args, should_parse, should_wait in steps:
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, timeout).until(element_present)
    element = driver.find_element_by_xpath(xpath)
    if should_wait:
        time.sleep(5)
    if should_parse:
        child_list = element.find_elements_by_tag_name("div")
        for child in child_list:
            text = child.text.replace(' ', "")
            if not text.startswith(':') and text != '(END)':
                strings.append(text)
    action = getattr(element, action)
    if args:
        action(args)
    else:
        action()

while not strings[-1].endswith('SuQmCC'):
    xpath, timeout, action, args, should_parse, should_wait = steps[-1]
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, timeout).until(element_present)
    element = driver.find_element_by_xpath(xpath)
    if should_wait:
        time.sleep(5)
    if should_parse:
        child_list = element.find_elements_by_tag_name("div")
        for child in child_list:
            text = child.text.replace(' ', "")
            if not text.startswith(':') and text != '(END)':
                strings.append(text)
    action = getattr(element, action)
    if args:
        action(args)
    else:
        action()

with open('strings.pkl', 'wb') as f:
    pickle.dump(strings, f)


