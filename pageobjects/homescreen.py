from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage
from values import strings

class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.title = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((
        #         By.TAG_NAME, "title")))    # can't locate title no trabajo

    # About shift link moved to Base- need to adjust accordingly @@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # self.cars_list = WebDriverWait(self.driver.instance, 10).until(
        #     EC.presence_of_all_elements_located((
        #         By.CLASS_NAME, "CarBrowser__list")))



    # def validate_title_is_present(self):
    #     assert self.title.is_displayed()

    # def validate_cars_list_is_visible(self):
    #     assert self.cars_list.is_displayed()