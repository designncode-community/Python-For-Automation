from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome('C:\chromedriver.exe')
driver.maximize_window()
url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver.get(url)
inputField = driver.find_element_by_xpath('//*[@id="user-message"]')
inputField.send_keys("Welcome To Python for Automation Session")
popup = driver.find_element_by_xpath('//*[@id="at-cv-lightbox-close"]')
popup.click()
showButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showButton.click()