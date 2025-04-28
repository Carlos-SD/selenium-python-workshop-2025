from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class SearchItem(BasePage):
    SEARCH_FIELD = (By.ID, 'cb1-edit')
    NAV_ICON = (By.XPATH, '/html/body/header/div/div[2]/form/button/div')
    ITEM_TAG = (By.XPATH, '/html/body/main/div/div[2]/aside/div[1]/ol/li[3]/a/span')

    def search_item(self, item):
        self.enter_text(self.SEARCH_FIELD, item)
        self.click(self.NAV_ICON)

    def isElementPresent(self):
        elemento = self.find_element(self.ITEM_TAG)
        texto = elemento.text
        return texto