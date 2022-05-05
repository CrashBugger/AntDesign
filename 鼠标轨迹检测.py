from selenium import webdriver
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get(r'http://www.porters.vip/captcha/mousemove.html')
    hover = browser.find_element_by_class_name('button1')
    actions = ActionChains(driver=browser)
    actions.click_and_hold(hover).perform()
    # actions.move_by_offset(340, 5)
    actions.move_by_offset(100,3)
    actions.move_by_offset(40,-5)
    actions.move_by_offset(10,3)
    actions.move_by_offset(5,2)
    actions.move_by_offset(40,3)
    actions.move_by_offset(30,7)
    actions.move_by_offset(34,-8)
    actions.move_by_offset(23,3)
    actions.release().perform()
