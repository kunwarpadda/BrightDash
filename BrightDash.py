import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Browser:
    browser, service = None, None

    def __init__(self, driver: str, option):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service,options=option)

    def open_site(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()

    def login(self, username: str, password: str):
        self.add_input(by=By.ID, value='username', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.CLASS_NAME, value='btn-primary')


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    username = os.environ.get("Bright_user") # Here either you can remove 'os.environ.get("Bright_user")' and write your username or you can define Environmental Variable in your OS as Bright_user containing your username
    password = os.environ.get("Bright_pass") # Here either you can remove 'os.environ.get("Bright_pass")' and write your password or you can define Environmental Variable in your OS as Bright_pass containing your password
    
    print("1. Online Tools")
    print("2. Crowdmark")
    print("3. Brightspace")
    
    user_input = input("Enter Your Choice: ")
    
    browser = Browser("chromedriver-win64\\chromedriver.exe",chrome_options)
    
    if user_input == "1":
        browser.open_site('https://www.uvic.ca/cas/login?service=https%3A%2F%2Fwww.uvic.ca%2Ftools%2Findex.php')
        
        browser.login(username, password)
    
    elif user_input == "2":
        browser.open_site("https://app.crowdmark.com/sign-in/university-of-victoria")
        browser.click_button(by=By.CLASS_NAME, value="button")
        browser.login(username, password)
        
    else:
        browser.open_site('https://www.uvic.ca/cas/login?service=https%3a%2f%2fbright.uvic.ca%2fd2l%2fcustom%2fcas%3ftarget%3d%252fd2l%252fhome')

        browser.login(username, password)
    