from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import asyncio
import aiohttp
import base64

from typing import Coroutine
from pathlib import Path
import time
from datetime import datetime
import random as rd

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
        """
        Fetches an image from a given URL and saves it to a local file.
        This method handles two types of image data:
        1. Base64 encoded data URLs.
        2. Normal encrypted URLs.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for making HTTP requests.
            url (str): The URL of the image to fetch.
        Returns:
            Coroutine: A coroutine that fetches the image and saves it to a file.
        """
        im_path = Path(self.path) / self._get_random_name() # generating random name for the file

        # 2 different types of stored data on google images
        if url.startswith("data"):  # base64 encoded
            extension = self._get_extension_data(url)
            try:
                encoded_data = url.split(f'data:image/{extension};base64,')[1] # getting the encoded data

                with open(im_path.with_suffix(".jpg"), 'wb') as file:
                    file.write(base64.b64decode(encoded_data))

            except Exception as exception_fetch_v1:
                print(exception_fetch_v1)
                
        else:   # normal encrypted url
            async with session.get(url) as response: # getting all of the images asynchronously
                with open(im_path.with_suffix(".jpg"), 'wb') as file:
                    file.write(await response.read())

    async def download_images(self, urls: list) -> Coroutine:
        """
        Downloads images from a list of URLs asynchronously.

        Args:
            urls (list): A list of image URLs to download.
        Returns:
            Coroutine: An asyncio coroutine that downloads the images.
        """
        async with aiohttp.ClientSession() as session:
            # creating tasks for every url
            tasks = [self.fetch_image(session, url) for url in urls]
            await asyncio.gather(*tasks)

    def execute_and_encode(self) -> None:
        """
        Starts all the processes in order to downlad the images.
        """
        try:    # creating a directory for the images
            self.path.mkdir(parents=True, exist_ok=True)
        except Exception as exception_mkdir:
            print(exception_mkdir)

        self.driver.get(self.endpoint)  # opening the google images page
        self._accept_cookies()
        self._render_images()   # scrolling down for 10s
        time.sleep(1)

        images = self.driver.find_elements(By.TAG_NAME, 'img')  # getting all of the images
        
        urls = self._filter_images(images)  # getting only the urls of the real images
        self.driver.quit()

        asyncio.run(self.download_images(urls))  # downloading the images asynchronously
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
    
    def _scroll_down(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _render_images(self) -> None:
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < 10:
            self._scroll_down()
    
    def _accept_cookies(self) -> None:
        """
        Accepts the cookies on the website via different methods.
        """
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




