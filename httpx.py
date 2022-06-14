import logging
import multiprocessing.pool
import re
from urllib.parse import urljoin

import requests

baseUrl = "https://ssr1.scrape.center"
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(leveltime)s:%(message)s')
totalPage = 10


def scrape_page(url: str):
    logging.info("scraping %s...", url)
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        logging.error("get invalid status code %s while scraping %s", resp.status_code, url)
    except requests.RequestException:
        logging.error('error occured while scraping %s', url, exc_info=True)


def scrape_Index(num):
    url = f'{baseUrl}/page/{num}'
    return scrape_page(url)


def parse_INdex(html):
    pattern = re.compile('<a.*?href="(.*?)" class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    else:
        for item in items:
            detail_url = urljoin(baseUrl, item)
            logging.info("get detail url %s", detail_url)
            yield item


def scrap_detail(url):
    return scrape_page(url)


def parse_detail(html):
    cover_pattern = re.compile('<img.*?src="(.*?)" class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile("""button.*?category.*?<span>(.*?)</span>.*?button""")
    published_at_pattern = re.compile("""<div.*?class.*?><span.*?>(\d{4}-\d{2}-\d{2})\s?上映""")
    drame_pattern = re.compile("""<h3.*？>剧情简介</h3><p.*?>(.*?)</p>""", re.S)
    score_pattern = re.compile("""<p.*?score.*?">(.*?)</p>""")
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html).group(1) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    drama = re.search(drame_pattern, html).group(1) if re.search(drame_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1)) if re.search(score_pattern, html) else None
    return {'cover': cover, 'name': name, 'categories': categories, 'published_at': published_at, "drama": drama,
            "score": score}


def main(page):
    html = scrape_Index(page)
    detail_urls = parse_INdex(html)
    for detail_url in detail_urls:
        detail_url = urljoin(baseUrl, detail_url)
        detail = scrap_detail(detail_url)
        data = parse_detail(detail)
        logging.info("get detail%s", data)
    logging.info("detail urls %s", list(detail_urls))


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    panges = range(1, totalPage + 1, 1)
    pool.map(main, panges)
    pool.close()
    pool.join()
    print("run main")
