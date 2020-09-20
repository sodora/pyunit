from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ChromeOptions


class Selenium(object):
    def __init__(self):
        opts = ChromeOptions()
        opts.add_argument('--incognito')
        capabilities = opts.to_capabilities()
        self.driver = WebDriver('http://127.0.0.1:4444/wd/hub', capabilities)

    def open_url(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

    def title(self):
        return self.driver.title
