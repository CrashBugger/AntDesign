import hashlib
import re
from urllib import parse

import requests
from fontTools.ttLib import TTFont
from parsel import Selector

if __name__ == '__main__':
    base_font = {
        "font": [{"name": "unie", "value": "", "hex": ""}]
    }
    url = "http://www.porters.vip/confusion/movie.html"
    resp = requests.get(url)
    sel = Selector(resp.text)
    # 提取页面加载的所有css路径
    # rel属性筛选，拿到href
    css_path = sel.css('link[res=stylesheet]::attr(href)').extract()
    woffs = []
    for c in css_path:
        # 拼接正确的css文件路径
        css_url = parse.urljoin(url, c)
    css_resp = requests.get(css_url)
    # 匹配css文件中的woff路径
    woff_path = re.findall("src:url\('..(.*.woff)'\)format\('woff'\);", css_resp.text)
    if woff_path:
        # 路径存在则添加到woffs列表
        woffs += woff_path
    woff_url = "https:www.porters.vip/confusion" + woffs.pop()
    woff = requests.get(woff_url)
    filename = 'target.woff'
    with open(filename, 'wb') as f:
        # 保存文件到本地
        f.write(woff.content)
    # 使用TTFont库打开文件
    font = TTFont(filename)
    web_code = '&#xe624.&#xe9c7'
    # 编码文字替换
    woff_code = [i.upper().replace('&#', 'uni') for i in web_code.split('.')]
    result = []
    for w in woff_code:
        # 从字体文件中取出对应编码信息
        content = font['glyf'].glyphs.get(w).data
    # 字形信息MD5
    glyph = hashlib.md5(content).hexdigest()
    for b in base_font.get('font'):
        # 与基准字形的MD5进行对比，相同则取出该字形的描述文字
        if b.get('hex') == glyph:
            result.append(b.get("value"))
            break
    print(result)
