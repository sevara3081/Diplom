from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchByTitle:
    def __init__(self, driver, book_title):
        self.driver = driver
        self.book_title = book_title
        self.search_input_xpath = '//*[@id="__layout"]/div/header/div/div[1]/div[2]/div/form/input'

    def search(self):
        search_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.search_input_xpath))
        )
        search_input.clear()
        search_input.send_keys(self.book_title)
        search_input.send_keys(Keys.ENTER)

    def get_results(self):
        results = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.catalog-search-products"))
        )
        return results