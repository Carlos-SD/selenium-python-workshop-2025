from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class SearchArticle(BasePage):
    SEARCH_FIELD = (By.NAME, 'search')
    NAV_ICON = (By.XPATH,'/html/body/div[1]/header/div[2]/div/div/div/form/div/button')
    ARTICLE_TITLE = (By.XPATH, '/html/body/div[2]/div/div[3]/main/header/h1/span')

    def search_item(self, item):
        self.enter_text(self.SEARCH_FIELD, item)
        self.click(self.NAV_ICON)

    def isElementPresent(self):
        elemento = self.find_element(self.ARTICLE_TITLE)
        texto = elemento.text
        return texto