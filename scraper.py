import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import time
import requests
from datetime import datetime

COOKIE_ACCEPT = '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button'
MORE_BUTTON = '//*[@id="islmp"]/div/div/div[1]/div/div[2]/span'
SCROLLS = 0
DIR = 'product'

COOKIES_XPATH = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span"
COOKIES_XPATH2 = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/div[3]"
COOKIES_TEXT = "//span[text()='Accept all'] | //div[text()='Accept all']"


MORE_BUTTON_1 = "//span[text()='Accept all'] | //div[text()='Accept all']"


class Scraper:

    def __init__(self, image_name, directory=DIR):

        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--lang=en-GB")

        self.dir = directory
        self.name = image_name
        self.endpoint = f'https://www.google.com/search?rlz=1C1YTUH_plPL1051PL1051&q={self.name}&tbm=isch&sa=X&ved' \
                        f'=2ahUKEwjXg4Phle3_AhWQgSoKHb78AW0Q0pQJegQICxAB&biw=1182&bih=754&dpr=1.25 '
        self.path = f'{self.dir}\\{self.name}'
        print(self.path)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.execute_and_encode()


    def accept_cookies(self):
        try:
            cookies = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, COOKIES_TEXT)))
            cookies.click()
            
        except ElementClickInterceptedException:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            cookies.click()
        except TimeoutException as e:
            print("COOKIES:", e)
            try:
                cookies = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, COOKIES_XPATH2)))
                cookies.click()
            except Exception as e:
                print("COOKIES:", e)
                try:
                    cookies = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, COOKIES_XPATH)))
                    cookies.click()
                except Exception as e:
                    print("COOKIES:", e)
                    time.sleep(30)


    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        


    def execute_and_encode(self):
        try:
            os.mkdir(self.path)
        except OSError as error:
            print(error)

        self.driver.get(self.endpoint)
        self.accept_cookies()

        print("SCROLLS:", SCROLLS)
        start = datetime.now()

        while True:
            self.scroll_down()
            if (datetime.now() - start).total_seconds() > 10:
                break
            

        time.sleep(1)
        images = self.driver.find_elements(By.TAG_NAME, 'img')
        print(len(images))

        counter = 0
        for im in images:
            extension = ''
            img_src = im.get_attribute('src')
            height = im.get_attribute('height')
            
            if img_src is not None and "FAVICON" not in img_src and "google" not in img_src and int(height) > 60:
                print(img_src)
                if img_src.startswith('data'):
                    extension = img_src[11:15]
                    if extension.endswith(';'):
                        extension = extension[:-1]
                #print(extension)

                to_decode = img_src.split(f'data:image/{extension};base64,')
                im_path = self.path + f'\\{self.name}{counter}'
                if len(to_decode) > 1:
                    with open(im_path + f'.jpg', 'wb') as file:
                        file.write(base64.b64decode(to_decode[1]))
                else:
                    respond = requests.get(img_src)
                    with open(im_path + '.jpg', 'wb') as file:
                        file.write(respond.content)
                counter += 1
        time.sleep(3)
        print('finished')
