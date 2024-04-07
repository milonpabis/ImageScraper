import requests
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random as rd

ENDPOINT = "https://www.pexels.com/search/"
COOKIES_TEXT = "//span[text()='Accept All Cookies'] | //div[text()='Accept All Cookies'] | //button[text()='Accept All Cookies']"

class ScraperV2:

    def __init__(self, output_path: str) -> None:
        self.output = output_path

    
    def run(self, word: str, num: int) -> None:
        urls = self._get_urls(word, num)
        self._download_images(urls)

    
    def _get_urls(self, word: str, num: int) -> list[str]:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--lang=en-GB")
        driver = webdriver.Chrome(chrome_options)
        driver.get(ENDPOINT + word)
        try:
            cookies = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, COOKIES_TEXT)))
            cookies.click()
        except Exception as e:
            print(e)

        images = driver.find_elements(By.TAG_NAME, "img")

        urls = [image.get_attribute("src") for image in images]
        clean_urls = self._filter_urls(urls)

        return clean_urls
    

    def _download_images(self, urls: list[str]) -> None:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        for url in urls:
            print(url)
            try:
                response = requests.get(url, headers=headers)
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    print("DOWNLOAD ERROR:", e)
                with open(self.output + str(rd.randint(1, 999999999999)) + ".jpg", "wb") as file:
                    file.write(response.content)
            except Exception as e:
                print(":C", e)


    def _filter_urls(self, urls: list[str]) -> list[str]:
        urls = list(filter(lambda u: "/photos/" in u, urls))
        return list(map(lambda u: u.split("?auto")[0], urls))
        


scr = ScraperV2("F:/Desktop/TEST/")
scr.run("cat", 10)
