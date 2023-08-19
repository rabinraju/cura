import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from selenium import webdriver
from cura.cura_login import cura
from cura.untill import wait_for_dahboard


class CuraTestCase(unittest.TestCase):
    driver = None

    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(4)
        cls.driver.get("https://katalon-demo-cura.herokuapp.com/")
        cls.driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()

        json_file_path = "C:\\Users\\antho\\PycharmProjects\\pythonProject3\\cura\\test_data.json"

        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

    @classmethod
    def tearDownClass(cls) -> None:
        print("sucessfully login")

    def test_asucessfully(self):
        curahs = cura(self.driver)
        curahs.input_username((self.data_dict.get("Login_test_data").get("correct_username")))
        time.sleep(2)
        curahs.input_password((self.data_dict.get("Login_test_data").get("correct_password")))
        time.sleep(2)
        curahs.click_login()
        time.sleep(2)
        assert wait_for_dahboard(self.driver)
        time.sleep(2)

    def test_bappointment(self):
        info = cura(self.driver)
        info.choose()
        time.sleep(2)
        info.click_radio_button()
        time.sleep(2)
        info.click_calendar()
        time.sleep(2)
        info.click_month()
        time.sleep(3)
        info.click_focused()
        time.sleep(2)
        info.click_datepikker()
        time.sleep(2)
        info.input_comment("Its Emergency")
        time.sleep(2)
        info.click_submit()
        time.sleep(3)
        info.click_backtodashboard()
        time.sleep(3)

    def tearDown(self) -> None:
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-bars']").click()
        time.sleep(4)
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='authenticate.php?logout']")))
        time.sleep(5)
        logout_button.click()
        time.sleep(7)

    def test_donceagain(self):
        self.driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()
        time.sleep(4)
        again = cura(self.driver)
        again.input_username(self.data_dict.get("Login_test_data").get("incorrect_username"))
        time.sleep(2)
        again.input_password(self.data_dict.get("Login_test_data").get("incorrect_password"))
        time.sleep(2)
        again.click_login()
        time.sleep(2)


