import asyncio
from time import sleep

from pyppeteer import launch
import logging

from pyppeteer.browser import Browser
from pyppeteer.page import Page

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')
INDEX_URL = "https://spa2.scrape.center/page/{page}"
TIMEOUT = 20
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False
browser: Browser = None
tab: Page = None


async def init():
    global browser, tab
    browser = await launch(devtools=True,
                           args=['--disable_inforbars', f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
    tab = await  browser.newPage()
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


async def scrape_page(url, selector):
    logging.info("scraping %s", url)
    try:
        await  tab.goto(url)
        await tab.waitForSelector(selector, options={'timeout': TIMEOUT * 1000})
    except TimeoutError:
        logging.error('error occured while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')


async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes =>nodes.map(node =>node.href)')


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            details_urls = await parse_index()
            logging.info('detail_urls', details_urls)
    finally:
        await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
