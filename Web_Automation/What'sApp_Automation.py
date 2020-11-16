import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/Users/zakaria/Downloads/chromedriver')
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')

driver.find_element_by_css_selector("span[title='" + input("Enter the Receiver Name: ") + "']").click()

inputString = input("Enter message to send: ")

for i in range(1):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    time.sleep(1)
    driver.find_element_by_css_selector("span[data-icon='clip']").click();
    # add file to send by file path
    driver.find_element_by_css_selector("input[type='file']").send_keys("/Volumes/Zakaria/ins_text/IMG_5682.JPG");
    # click to send
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click();

