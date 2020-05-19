from __future__ import division
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys


class InstaBot:
    followersCount = 0
    followersList =[]
    followingCount = 0
    followingList = []
    ffDifference = 0
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def __log_in__(self):
        self.driver = webdriver.Chrome(r'C:\Users\Shreyas\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://instagram.com")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input") \
            .send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]") \
            .click()
        sleep(5)

    def __home__(self):
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]") \
            .click()
        sleep(2)
        #Enters user profile using one of two methods
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a") \
                .click()
            sleep(2)
        except:
            try:
                self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input") \
                    .send_keys(self.username)
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input") \
                    .send_keys(Keys.ENTER)
                sleep(1)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span") \
                    .click()
                sleep(2)
            except:
                raise("Could not find profile")

    def __names__(self,paths):
        self.driver.find_element_by_xpath(paths) \
            .click()
        sleep(1)
        popupBox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        tempHeight =1
        finalHeight =0
        #If suggestions box is present - modified counter
        try:
            suggestions = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
            self.driver.execute('arguments[0].scrollIntoView()',suggestions)
            sleep(2)
            while True:
                self.driver.execute_script("arguments[0].scrollTo(0,arguments[0].scrollHeight);",popupBox)
                sleep(0.8)
                tempHeight = self.driver.execute_script("return arguments[0].scrollHeight;",popupBox)
                if tempHeight == finalHeight:
                    break
                finalHeight = tempHeight

        except:
            try:
                while True:
                    self.driver.execute_script("arguments[0].scrollTo(0,arguments[0].scrollHeight);",popupBox)
                    sleep(0.8)
                    tempHeight = self.driver.execute_script("return arguments[0].scrollHeight;",popupBox)
                    if tempHeight == finalHeight:
                        break
                    finalHeight = tempHeight

            except:
                raise("Unable to scroll")

        links = popupBox.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button") \
            .click()
        return names

    def __unfollowers__(self):
        self.followersList = self.__names__("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        sleep(2)
        self.followingList = self.__names__("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        print("Follower to Following ratio",len(self.followersList)/len(self.followingList))
        notfollowBack = []
        for name in self.followingList:
            if(name not in self.followersList):
                notfollowBack.append(name)
        print("People who you follow but do not follow back: ",len(notfollowBack))
        print("List of those people: ",notfollowBack)

user = input("Enter your username: ")
passw = input("Enter your password: ")
bot = InstaBot(user,passw)
bot.__log_in__()
bot.__home__()
bot.__unfollowers__()
