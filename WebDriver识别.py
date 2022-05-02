import time

import selenium.webdriver
from selenium import webdriver

if __name__ == '__main__':
    # 被检测到了-----------------
    # driver = Chrome()
    # driver.get("http://www.porters.vip/features/webdriver.html")
    # driver.find_element_by_css_selector("button.btn.btn-primary.btn-lg").click()
    # elements = driver.find_element_by_css_selector("#content")
    # print(elements.text)
    driver = webdriver.Chrome()
    driver.get("http://www.porters.vip/features/webdriver.html")
    # 编写javascript

    time.sleep(1)
    driver.get("http://www.porters.vip/features/webdriver.html")
    #执行javascript
    script = """Object.defineProperty(navigator,"webdriver",{get: () => false,});"""
    driver.execute_script(script)
    driver.find_element_by_css_selector("button.btn.btn-primary.btn-lg").click()
    element = driver.find_element_by_css_selector("#content")
    #等待元素加载
    time.sleep(2)
    print(element.text)
