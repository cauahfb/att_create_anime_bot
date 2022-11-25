from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import time

class notionBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"geckodriver")

    def start_bot(self,sheets,anime_site,notion):
        self.driver.get(sheets)
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.driver.execute_script("window.open('');") 
        self.driver.switch_to.window(self.driver.window_handles[1])        
        self.driver.get(anime_site)

        self.driver.execute_script("window.open('');") 
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get(notion)
        time.sleep(5)
        
    def login_notion(self,email,password):
        act=ActionChains(self.driver)
        btn_login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/div[3]")
        btn_login.click()
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="notion-email-input-1"]')
        email_input.send_keys(email)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="notion-password-input-2"]')
        password_input.send_keys(password)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(2)

    def first_bot(self):

        self.driver.switch_to.window(self.driver.window_handles[0])
        act=ActionChains(self.driver)
        act.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        anime_box = self.driver.find_element(By.ID, "chart-search")
        anime_box.click()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.DELETE).perform()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(3)

        anime_card = self.driver.find_element(By.XPATH, '//*[@id="content"]/main/article[4]/div/div[2]')
        if anime_card.is_displayed():
            self.driver.switch_to.window(self.driver.window_handles[2])
            btn_search = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]")
            btn_search.click()
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(2)
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div").click()
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[4]/div/div[2]/div").click()
            act.send_keys(Keys.ARROW_DOWN).perform()
            act.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            act.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            act.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            bot.go_bot()
            
        else:
            bot.go_bot()

    def go_bot(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        act=ActionChains(self.driver)
        act.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        anime_box = self.driver.find_element(By.ID, "chart-search")
        anime_box.click()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.DELETE).perform()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(3)

        anime_card = self.driver.find_element(By.XPATH, '//*[@id="content"]/main/article[4]/div/div[2]')
        if anime_card.is_displayed():
            self.driver.switch_to.window(self.driver.window_handles[2])
            btn_search = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]")
            btn_search.click()
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(2)
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.TAB).perform()
            act.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[4]/div/div[2]/div").click()
            act.send_keys(Keys.ARROW_DOWN).perform()
            act.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            act.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            act.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            bot.go_bot()
            
        else:
            bot.go_bot()


bot = notionBot()
bot.open_sites(google_drive_link,"https://myanimelist.net",notion_link)
bot.login_notion(email,senha)
bot.first_bot()
