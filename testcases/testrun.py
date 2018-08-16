from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.shift.com/")
# signin = driver.find_element_by_class_name("ft-auth-sign-in")
# account_panel = driver.find_element_by_class_name("ft-user-name")

# hover = ActionChains(driver).move_to_element(account_panel)
# hover.perform()
# time.sleep(1)
# signin.click()
# time.sleep(1)

link = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/header/nav/ul/li[5]/a/span")
link.click()
time.sleep(2)
car_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/a/button")
#email_field.send_keys("alexbichevoy211@gmail.com")
car_button.click()
time.sleep(2)
driver.back()

meet_our_concierges = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[5]/div/div[3]/div[2]/a")
#signin_button = driver.find_element_by_id("loginButton")
#pass_field.send_keys("KseniBi211")
meet_our_concierges.click()
time.sleep(2)
driver.back()
time.sleep(2)
