from selenium import webdriver

browser= webdriver.Chrome('./chromedriver.exe')

browser.maximize_window()
browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in browser.title
button=browser.find_element_by_class_name('btn-primary')
print(button.get_attribute('innerHTML'))

assert 'Show Message' in browser.page_source

message=browser.find_element_by_id('user-message')
button2= browser.find_element_by_css_selector('#get-input > .btn')
print(button2)
message.clear()
message.send_keys('message sent')

button.click()
output_message= browser.find_element_by_id('display')
assert 'message sent' in output_message.text

browser.close()