import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import time
from datetime import datetime
import random as rd
from typing import Coroutine

import asyncio
import aiohttp
from pathlib import Path

from static import *



class Scraper:


    def __init__(self, image_name, directory=DIR):
        self.name = image_name
        self.endpoint = ENDPOINT_GOOGLE % self.name
        self.path = Path(directory) / self.name

        chrome_options = self._get_chrome_options(headless=False)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.execute_and_encode()   # starting the process

    

    async def fetch_image(self, session: aiohttp.ClientSession, url: str) -> Coroutine:
        im_path = Path(self.path) / self._get_random_name()
        print("starting: ", url)
        if url.startswith("data"):
            extension = self._get_extension_data(url)
            try:
                encoded_data = url.split(f'data:image/{extension};base64,')[1]

                with open(im_path.with_suffix(".jpg"), 'wb') as file:
                    file.write(base64.b64decode(encoded_data))

            except Exception as exception_fetch_v1:
                print(exception_fetch_v1)
                
        else:
            async with session.get(url) as response:
                with open(im_path.with_suffix(".jpg"), 'wb') as file:
                    file.write(await response.read())

    

    async def download_images(self, urls: list) -> Coroutine:
        async with aiohttp.ClientSession() as session:
            # creating tasks for every url
            tasks = [self.fetch_image(session, url) for url in urls]
            await asyncio.gather(*tasks)



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
        
        urls = self._filter_images(images)
        self.driver.quit()

        asyncio.run(self.download_images(urls))

        print("finished")

    
    def _get_extension_data(self, url: str) -> str:
        extension = url[11:15]
        if extension.endswith(';'):
            extension = extension[:-1]
        return extension
    

    def _get_random_name(self) -> str:
        return f"{self.name}{rd.randint(0, 999999999)}"
    

    def _check_image(self, image) -> bool:
        url, height = image.get_attribute('src'), image.get_attribute('height')
        return url is not None and "FAVICON" not in url and "google" not in url and int(height) > 60
    

    def _filter_images(self, images) -> list:
        return [image.get_attribute("src") for image in images if self._check_image(image)]
    

    def _get_chrome_options(self, headless: bool = False) -> webdriver.ChromeOptions:
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--lang=en-GB")
        return chrome_options
