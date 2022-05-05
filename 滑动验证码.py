from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://www.porters.vip/captcha/sliders.html")
    hover = browser.find_element_by_css_selector(".hover")
    action = webdriver.ActionChains(browser)
    # 点击并保持吃不松开
    action.click_and_hold(hover).perform()
    # 设置滑动距离
    action.move_by_offset(340, 0)
    action.release().perform()
