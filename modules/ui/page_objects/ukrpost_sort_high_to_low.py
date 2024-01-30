from modules.ui.page_objects.ukrpost_base_page import UkrPostBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class UkrPostMainPage(UkrPostBasePage):
    URL = "https://postmark.ukrposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(UkrPostMainPage.URL)

    def search_merch(self):
        # Знаходимо категорію "Художні марки"
        art_stamp_cat = self.driver.find_element(By.XPATH, "//a[@class='list-group-item list-group-item_child']")

        # Клікаємо на категорію
        art_stamp_cat.click()

    def sort_high_to_low(self):

        # Знаходимо поле для сортування
        sort_field = self.driver.find_element(By.ID, "input-sort")

        # Клікаємо на поле для сортування
        sort_field.click()

        # Знаходимо поле сортування
        select_element = self.driver.find_element(By.ID, "input-sort")
        select = Select(select_element)

        # Знаходимо елемент "Ціна (За зменшенням)"
        self.driver.find_element(By.CSS_SELECTOR, "#input-sort>option:nth-child(5)")

        select.select_by_index(4)

    def check_url(self, expected_url):
        # Перевіряємо, що відкрита правильна сторінка
        return self.driver.current_url == expected_url