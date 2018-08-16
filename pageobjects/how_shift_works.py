from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings
from selenium import webdriver
from pageobjects.basepage import BasePage


class HowShiftWorks(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.car_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/a/button")))
        self.browse_the_best = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//h3[text()='Browse the best']")))
        self.test_drives_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//h3[text()='Test drives, delivered']")))
        self.no_hassle_buying = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//h3[text()='No-hassle buying']")))
        self.see_for_yourself = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, "See for yourself")))
        self.inspection = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//div[@class='ContentToggle__root']//div[contains(text(),'See the full Shift inspection process')]")))
        self.meet_our_concierges = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Meet our Concierges')]")))
        self.read_reviews_on_yelp = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[@class='BuyerMarketing__link' and contains( text(),'Read reviews on Yelp')]")))
        self.browse_cars_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[@class='Button__content' and text()='Browse cars']")))


    def validate_select_car_button(self):
        assert self.car_button.is_displayed()

    def validate_browse_the_best_link(self):
        assert self.browse_the_best.is_displayed()

    def validate_test_drives_link(self):
        assert self.test_drives_link.is_displayed()

    def validate_no_hassle_buying(self):
        assert self.no_hassle_buying.is_displayed()

    def validate_see_for_yourself(self):
        assert self.see_for_yourself.is_displayed()

    def validate_inspection(self):
        assert self.inspection.is_displayed()

    def validate_meet_our_concierges(self):
        assert self.meet_our_concierges.is_displayed()

    def validate_read_reviews_on_yelp(self):
        assert self.read_reviews_on_yelp.is_displayed()

    def validate_browse_cars_btn(self):
        assert self.browse_cars_btn.is_displayed()





