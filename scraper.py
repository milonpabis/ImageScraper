import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import base64
import time
import requests

COOKIE_ACCEPT = '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button'
MORE_BUTTON = '//*[@id="islmp"]/div/div/div[1]/div/div[2]/span'
SCROLLS = 0
DIR = 'product'




class Scraper:

    def __init__(self, image_name, directory=DIR):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")

        self.dir = directory
        self.name = image_name
        self.endpoint = f'https://www.google.com/search?rlz=1C1YTUH_plPL1051PL1051&q={self.name}&tbm=isch&sa=X&ved' \
                        f'=2ahUKEwjXg4Phle3_AhWQgSoKHb78AW0Q0pQJegQICxAB&biw=1182&bih=754&dpr=1.25 '
        self.path = f'{self.dir}\\{self.name}'
        print(self.path)

        self.driver = webdriver.Chrome()
        self.execute_and_encode()


    def accept_cookies(self):
        time.sleep(1)
        try:
            cook = self.driver.find_element(By.XPATH, COOKIE_ACCEPT)
            cook.click()
        except NoSuchElementException:
            return


    def scroll_down(self):
        time.sleep(2)
        boolean = False
        try:
            more = self.driver.find_element(By.XPATH, MORE_BUTTON)
            time.sleep(1)
            more.click()
        except:
            boolean = True

        if boolean:
            try:
                more = self.driver.find_element(By.CLASS_NAME, 'LZ4I')
                time.sleep(1)
                more.click()
            except:
                print('scroll succesful')
                pass

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


    def execute_and_encode(self):
        try:
            os.mkdir(self.path)
        except OSError as error:
            print(error)

        self.driver.get(self.endpoint)
        self.accept_cookies()

        print("SCROLLS:", SCROLLS)
        for _ in range(SCROLLS):
            self.scroll_down()
            time.sleep(1)

        time.sleep(3)
        images = self.driver.find_elements(By.CLASS_NAME, 'rg_i')
        print(len(images))

        counter = 0
        for im in images:
            extension = ''
            img_src = im.get_attribute('src')
            print(img_src)

            if img_src is not None:

                if img_src.startswith('data'):
                    extension = img_src[11:15]
                    if extension.endswith(';'):
                        extension = extension[:-1]
                #print(extension)

                to_decode = img_src.split(f'data:image/{extension};base64,')
                im_path = self.path + f'\\{self.name}{counter}'
                if len(to_decode) > 1:
                    with open(im_path + f'.{extension}', 'wb') as file:
                        file.write(base64.b64decode(to_decode[1]))
                else:
                    respond = requests.get(img_src)
                    with open(im_path + '.jpeg', 'wb') as file:
                        file.write(respond.content)
                counter += 1
        time.sleep(3)
        print('finished')
