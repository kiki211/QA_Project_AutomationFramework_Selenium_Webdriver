import unittest
from pageobjects.homescreen import HomeScreen
from values import strings
from webdriver import Driver

class TCHomeScreen(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen(self):
        home_screen = HomeScreen(self.driver)
        # Upper MENU
        home_screen.validate_shift_icon_present()
        home_screen.validate_location_menu_present()
        home_screen.validate_heart_icon_id_present()
        home_screen.validate_browse_cars_present()
        home_screen.validate_sell_your_car_present()
        home_screen.validate_financing_present()
        home_screen.validate_how_shift_works_link_present()
        home_screen.validate_more_present()
        home_screen.validate_sign_in_present()
        # Others
        # home_screen.validate_cars_list_is_visible()

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()