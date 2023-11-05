# using python Testing_script automation and the url  display the cookie created  before login and after login in the console.after you login in the dashboard of the zen portal kindly do the logout also.
# verify that the cookies are being generated during the login process

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException

class Saucelab:
    login_id = "standard_user"
    password = "secret_sauce"
    def __init__(self, weburl):
        self.url = weburl
        # if we want run our automation script without opening browser,we use headless_option
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def before_login(self):
        try:
            self.driver.maximize_window()
            # browser navigate to webpage
            self.driver.get(self.url)
            sleep(3)
            # in Testing_script webdriver we can get web page cookie by using get_cookies()method
            # before login to sauce_lab
            before_login_cookie = self.driver.get_cookies()
            print("cookies before login:" , before_login_cookie)
        except NoSuchElementException as error:
            print(error)

    def after_login(self):
        try:
            # here  using Relative Xpath to find input_field element in html page
            username = self.driver.find_element(by=By.XPATH, value="//div[@class='form_group']/input[@id='user-name']")
            username.send_keys(self.login_id)
            sleep(4)
            # here  using Relative Xpath to find password_field element in html page
            password = self.driver.find_element(by=By.XPATH, value='//div[@class="form_group"]/following::input[@id="password"]')
            password.send_keys(self.password)
            sleep(4)
            # we use CssSelector to find login_button element
            login_button = self.driver.find_element(by=By.CSS_SELECTOR, value="input#login-button")
            login_button.click()
            sleep(3)
            # we get cookies after login to sauce_lab page
            cookies_after = self.driver.get_cookies()
            print("cookies after login: ",cookies_after)

            # now  verifying the cookies are printed after the login into sauce_lab webpage
            # we iterate the cookies
            # hence, cookies name are same and it is true
            for cookie in cookies_after:
                name = cookie['name']
                if cookie['name'] == name:
                    print(f"this cookie was generated during a login")
                else:
                    print("this cookie is not generated during login")

        except NoSuchElementException as no_element:
            print(no_element)

    def logout_webpage(self):
        try:
            # here  using Xpath locator to find Element of dashboard_menu
            dashboard_menu = self.driver.find_element(by=By.XPATH, value='//div[@class="bm-burger-button"]/button[@id="react-burger-menu-btn"]')
            dashboard_menu.click()
            sleep(3)
            # here also using Relative Xpath to find Logout_button
            logout_btn = self.driver.find_element(by=By.XPATH, value='//div[@class="bm-menu"]//a[text()="Logout"]')
            logout_btn.click()
        except NoSuchElementException as error:
            print(error)
        except ElementNotInteractableException as error2:
            print(error2)

    def shutdown(self):
        # close the webdriver
        self.driver.quit()

# main url
link = "https://www.saucedemo.com/"
# driver codes
data = Saucelab(link)
data.before_login()
data.after_login()
data.logout_webpage()
data.shutdown()
