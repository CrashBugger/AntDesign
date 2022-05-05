from PIL import Image, ImageChops
from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://www.porters.vip/captcha/jigsawCanvas.html")
    jigsawCircle = browser.find_element_by_css_selector("#jigsawCircle")
    # 定位背景图片
    jigsawCanvas = browser.find_element_by_css_selector("#jigsawCanvas")
    jigsawCanvas.screenshot('before.png')
    action = webdriver.ActionChains(browser)
    # 点击并保持不松开
    action.click_and_hold(jigsawCircle).perform()
    # 执行javascript隐藏圆角矩形的代码
    scripts = """
    var missblock=document.getElementById('missblock');
    missblock.style['visibility']='hidden';
    """
    browser.execute_script(scripts)
    # 再次截图
    jigsawCanvas.screenshot('after.png')
    # 开始对比图片
    image_a = Image.open('after.png')
    image_b = Image.open('before.png')
    # 对比像素不同
    diff = ImageChops.difference(image_a, image_b)
    # 获取图片差异位置坐标---上下左右
    diff_positions = diff.getbbox()
    position_x = diff_positions[0]
    action.move_by_offset(int(position_x) - 10, 0)
    action.release().perform()
