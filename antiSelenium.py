from selenium import webdriver
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    option = ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                            {'source': """Object.defineProperty(navigator,"webdriver",{get:() =>undefined})"""})
    browser.get("https://antispider1.scrape.center/")
