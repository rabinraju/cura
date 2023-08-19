from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cura:

    def __init__(self, driver):
        self.loginpage_driver = driver

    username_locator = "username"
    password_locator = "password"
    click_login_button = "//button[@id='btn-login']"
    choose_Facility = "// option[text() = 'Hongkong CURA Healthcare Center']"
    click_readmission = "//input[@id='chk_hospotal_readmission']"
    click_glyphicon_calendar = "//div[@class='input-group-addon']//span"
    current_month = "//th[@class='datepicker-switch'][1]"
    click_focusedmonth = "//span[@class='month focused']"
    click_visit_date = "//td[@class='day' and text()='22']"
    comment_locator = "comment"
    click_appointment = "//button[@id='btn-book-appointment']"
    click_dashboard = "//a[@class='btn btn-default']"
    click_appointment1 = "//button[@id='btn-book-appointment']"


    # login

    def input_username(self, username):
        self.loginpage_driver.find_element(By.NAME, self.username_locator).send_keys(username)

    def input_password(self, password):
        self.loginpage_driver.find_element(By.NAME, self.password_locator).send_keys(password)

    def click_login(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.click_login_button).click()

    def choose(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.choose_Facility).click()

    def click_radio_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.click_readmission).click()

    def click_calendar(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.click_glyphicon_calendar).click()

    def click_month(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.current_month).click()

    def click_focused(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.click_focusedmonth).click()

    def click_datepikker(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.click_visit_date).click()

    def input_comment(self, comment):
        self.loginpage_driver.find_element(By.NAME, self.comment_locator).send_keys(comment)

    def click_submit(self):
        self.loginpage_driver.find_element(By.XPATH, self.click_appointment).click()

    def click_backtodashboard(self):
        self.loginpage_driver.find_element(By.XPATH, self.click_dashboard).click()



# Again
#     def click_submit1(self):
#         self.loginpage_driver.find_element(By.XPATH, self.click_appointment1).click()