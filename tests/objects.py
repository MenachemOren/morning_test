import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Objects:

    def __init__(self):
        self.chrome_options = Options()
        self.edge_options = Options()
        self.driver1 = None
        self.driver2 = None
        self.action_chains = None
        self.edit_profile = None
        self.interests = None
        self.name = None
        self.mail = None
        self.update_profile = None
        self.mongo_name = None
        self.mongo_mail = None
        self.mongo_interests = None
        self.open_page()
        self.open_mongo_page()
        self.set_elements()

    def open_page(self):
        self.driver1 = webdriver.Chrome(options=self.chrome_options)
        self.driver1.get("http://localhost:3000/")

    def open_mongo_page(self):
        self.driver2 = webdriver.Chrome(options=self.chrome_options)
        self.driver2.get("http://localhost:8080/db/my-db/users")

    def get_browser(self):
        return "chrome"


    def set_elements(self):
        self.edit_profile = self.driver1.find_element_by_xpath('//*[@id="container"]/button').click()
        self.name = self.driver1.find_element_by_xpath('//*[@id="input-name"]')
        self.mail = self.driver1.find_element_by_xpath('//*[@id="input-email"]')
        self.interests = self.driver1.find_element_by_xpath('//*[@id="input-interests"]')
        self.update_profile = self.driver1.find_element_by_xpath('//*[@id="container-edit"]/button')
        self.mongo_name = self.driver2.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/table/tbody/tr/td[5]')
        self.mongo_mail = self.driver2.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/table/tbody/tr/td[3]')
        self.mongo_interests = self.driver2.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/table/tbody/tr/td[4]')

    def edit_name(self, name):
        time.sleep(2)
        self.name.clear()
        self.name.send_keys(name)
        time.sleep(2)

    def edit_mail(self, mail):
        time.sleep(2)
        self.mail.clear()
        self.mail.send_keys(mail)
        time.sleep(2)

    def update(self):
        self.update_profile.click()
        time.sleep(2)

    def edit_interests(self, interests):
        time.sleep(2)
        self.interests.clear()
        self.interests.send_keys(interests)
        time.sleep(2)

    def close_drivers(self):
        self.driver1.close()
        self.driver2.close()

    def get_mongo_name(self):
        return self.mongo_name.text

    def get_mongo_mail(self):
        return self.mongo_mail.text

    def get_mongo_interests(self):
        return self.mongo_interests.text



