from modules.ui.page_objects.makeup_base_page import BasePageMakeup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MakeupMainPage(BasePageMakeup):
    URL = 'https://makeup.com.ua/ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(MakeupMainPage.URL)

    def go_to_makeup_youtube(self):
        # Знаходимо іконку(кнопку) ютубу на сторінці
        yt_btn = self.driver.find_element(By.XPATH, "//li[@class='social__item social-icon yt']")
        actions = ActionChains(self.driver)
        actions.move_to_element(yt_btn).perform()

        yt_btn.click()

    def check_url(self, expected_url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url == expected_url
    
    def close_brwsr(self):
        self.driver.quit()