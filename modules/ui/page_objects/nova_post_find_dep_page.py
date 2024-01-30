from modules.ui.page_objects.nova_post_base_page import BasePageNovaPost
from selenium.webdriver.common.by import By

class FindDepPage(BasePageNovaPost):
    URL = 'https://novapost.com/uk-ua/departments?city=118064'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(FindDepPage.URL)

    def click_survey(self):
        # Знаходимо кнопку "Закрити" в опитувальнику
        surv_btn = self.driver.find_element(By.CSS_SELECTOR, 'button.css-1ftaqxs')

        # Закриваємо опитувальник
        surv_btn.click()

    def try_search(self, department):
        # Знаходимо поле куди будемо вводити неправильний номер відділення
         dep_elem = self.driver.find_element(By.NAME, "address")

        # Вводимо неправильний номер відділення
         dep_elem.send_keys(department)
        
    def check_title(self):
        # Знаходимо текст
        not_found_text = self.driver.find_element(By.CSS_SELECTOR, "div.department-data-group>h4+div")
        assert not_found_text