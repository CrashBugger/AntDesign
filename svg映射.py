import re
from parsel import Selector

import requests

if __name__ == '__main__':
    url_css = "http://www.porters.vip/confusion/css/food.css"
    url_svg = "http://www.porters.vip/confusion/font/food.svg"
    css_resp = requests.get(url_css).text
    svg_resp = requests.get(url_svg).text
    css_class_name = 'vhkbvu'
    pile = '.%s{background:-(\d+)px-(\d+)px;}' % css_class_name
    pattern = re.compile(pile)
    # 链式编程,文本清洗
    css = css_resp.replace('\n', '').replace(' ', '')
    #得到元组
    coord = pattern.findall(css)
    # 列表非空
    if coord:
        x, y = coord[0]
        x, y = int(x), int(y)
    # 得到坐标正值
    #Selector定位
    svg_data = Selector(svg_resp)
    texts = svg_data.xpath('//text')
    # 拿到最近的y标签
    axis_y = [i.attrib.get('y') for i in texts if y <= int(i.attrib.get('y'))][0]
    # 确定那个text标签
    svg_text = svg_data.xpath('//text[@y="%s"]/text()' % axis_y).extract_first()
    font_size = re.search('font-size:(\d+)px', svg_resp).group(1)
    # 地板除法拿到位置
    position = x // int(font_size)
    number = svg_text[position]
    print(number)
