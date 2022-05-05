import re
from parsel import Selector
from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://www.porters.vip/captcha/jigsaw.html")
    jigsaw = browser.find_element_by_css_selector("#jigsawCircle")
    # 点击并保持不松开
    action = webdriver.ActionChains(browser)
    action.click_and_hold(jigsaw).perform()
    # 当前页面元源码
    html = browser.page_source
    sel = Selector(html)
    # 获取圆角矩形和缺口的css样式
    mbk_style = sel.css('#missblock::attr("style")').get()
    tbk_style = sel.css('#targetblock::attr("style")').get()
    # 编写匿名函数从css中提取left属性
    extract = lambda x: ''.join(re.findall('left:\s?(\d+|\d+.\d+)px', x))
    # 调用匿名函数获取css样式中的left属性
    mbk_left = extract(mbk_style)
    tbk_left = extract(tbk_style)
    # 计算当前拼图验证码所需移动距离
    distance = float(tbk_left) - float(mbk_left)
    action.move_by_offset(distance, 0)
    action.release().perform()
