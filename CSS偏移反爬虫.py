import re

import requests
from parsel import Selector

if __name__ == '__main__':
    url = "http://www.porters.vip/confusion/flight.html"
    resp = requests.get(url)
    sel = Selector(resp.text)
    em = sel.css("em.rel").extract()
    for element in em:
        element = Selector(element)
        element_b = element.css('b').extract()
        bl = Selector(element_b.pop(0))
        base_price = bl.css('i::text').extract()
        alternate_price = []
        print(element_b)
        for eb in element_b:
            eb = Selector(eb)
            # 提取b标签style属性值
            style = eb.css('b::attr("style")').get()
            position = ''.join(re.findall('left:(.*)px', style))
            # 获取改标签下的数字
            value = eb.css('b::text').get()
            # 将b标签的位置信息和数字以字典的格式添加到替补票价列表中
            alternate_price.append({'position': position, 'value': value})
        # 然后决定覆盖元素
        for al in alternate_price:
            position = int(al.get('position'))
            # 判断位置的数值是否为正整数
            plus = True if position >= 0 else False
            # 计算下标，以16px为基准
            index = int(position / 16)
            # 替换第一对《b》标签列表中的元素
            base_price[index] = value
        print(base_price)
