import io
from urllib.parse import urljoin

import pytesseract as pytesseract
import requests
from PIL.Image import open
from parsel import Selector

if __name__ == '__main__':
    url = "http://www.porters.vip/confusion/recruit.html"
    resp = requests.get(url)
    sel = Selector(resp.text)
    # 从响应正文提取图片名称
    image_name = sel.css('.pn::attr("src")').extract_first()
    # 拼接图片名和url
    image_url = urljoin(url, image_name)
    # 请求图片拿到图片字节流内容
    image_body = requests.get(image_url).content
    # 使用image.open打开图片字节流，得到图片对象
    image_stream = open(io.BytesIO(image_body))
    # 使用光学字符识别从图片对象中读取文字并打印输出结果
    print(pytesseract.image_to_string(image_stream))
