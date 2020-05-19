from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class InstaBot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome(r'C:\Users\Shreyas\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(password)
        sleep(5)
        self.driver.quit()

user = input("Enter your username: ")
passw = input("Enter your passwSord: ")
InstaBot(user,passw)
