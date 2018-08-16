import pytest as pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver
   # **********************   UPPER MENU   ***********************

        self.shift_icon = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "SiteChromeHeader__shift-logo")))

        self.location_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "chosen-container-single-nosearch")))

        self.heart_icon = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "CarFavoritesHeaderHeart__heart-container")))

        self.browse_cars = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, "Browse cars")))

        self.sell_your_car = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, "Sell your car")))

        self.financing = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, "Financing")))

        self.how_shift_works_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, "How Shift works")))

        self.more = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "SiteChromeHeader__more-li")))

        self.sign_in = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, "Sign in")))



    def validate_shift_icon_present(self):
        assert self.shift_icon.is_displayed()

    def validate_location_menu_present(self):
        assert self.location_menu.is_displayed()

    def validate_heart_icon_id_present(self):
        assert self.heart_icon.is_displayed()

    def validate_browse_cars_present(self):
        assert self.browse_cars.is_displayed()

    def validate_sell_your_car_present(self):
        assert self.sell_your_car.is_displayed()

    def validate_financing_present(self):
        assert self.financing.is_displayed()

    def validate_how_shift_works_link_present(self):
        assert self.how_shift_works_link.is_displayed()

    def validate_more_present(self):
        assert self.more.is_displayed()

    def validate_sign_in_present(self):
        assert self.sign_in.is_displayed()


  # Add more functions with shared web elements across the site


    # def validate_icon_is_present(self):
    #     icon = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((
    #             By.CLASS_NAME, "custom-logo")))
    #     assert icon.is_displayed()
    #
    # def validate_menu_options_are_present(self):
    #     top_menu = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((
    #             By.ID, "top-menu")))
    #     assert top_menu.is_displayed()
    #
    # def validate_social_media_links(self):
    #     twitter_button = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((
    #             By.XPATH, "//span[contains(text(), 'Twitter')]")))
    #     linkedin_button = WebDriverWait(self.driver.instance, 10).until(
    #         EC.visibility_of_element_located((
    #             By.XPATH, "//span[contains(text(), 'LinkedIn')]")))
    #     assert twitter_button.is_displayed()
    #     assert linkedin_button.is_displayed()


