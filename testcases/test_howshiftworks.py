import unittest
from pageobjects.how_shift_works import HowShiftWorks
from pageobjects.homescreen import HomeScreen
from webdriver import Driver
from values import strings
from pageobjects.basepage import BasePage

class TCHowShiftWorks(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.how_shift_works_url)


    def test_how_shift_works_components(self):
        how_shift_works = HowShiftWorks(self.driver)
       # Upper Menu
        how_shift_works.validate_shift_icon_present()
        how_shift_works.validate_location_menu_present()
        how_shift_works.validate_heart_icon_id_present()
        how_shift_works.validate_browse_cars_present()
        how_shift_works.validate_sell_your_car_present()
        how_shift_works.validate_financing_present()
        how_shift_works.validate_how_shift_works_link_present()
        how_shift_works.validate_more_present()
        how_shift_works.validate_sign_in_present()
        # Buttons ans links
        how_shift_works.validate_browse_the_best_link()
        how_shift_works.validate_test_drives_link()
        how_shift_works.validate_no_hassle_buying()
        how_shift_works.validate_see_for_yourself()
        how_shift_works.validate_inspection()
        how_shift_works.validate_read_reviews_on_yelp()
        how_shift_works.validate_meet_our_concierges()
        how_shift_works.validate_browse_cars_btn()


    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()
