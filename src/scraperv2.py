import requests
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime as dt

ENDPOINT = "https://www.pexels.com/search/"
COOKIES_TEXT = "//span[text()='Accept All Cookies'] | //div[text()='Accept All Cookies'] | //button[text()='Accept All Cookies']"

class ScraperV2:

    def __init__(self, output_path: str) -> None:
        self.output = output_path

    
    def run(self, word: str, num: int, hq: bool = True) -> None:
        if not os.path.exists(self.output):
            os.makedirs(self.output, exist_ok=True)

        urls = self._get_urls(word, num, hq=hq)
        self._download_images(urls)

    
    def _get_urls(self, word: str, num: int, hq: bool = True) -> list[str]:
        """
        Scrapes the urls from the website.

        Args:
        - word: the word to be searched.
        - num: number of images to be downloaded.
        - hq: if True, returns only high quality images urls.

        Returns:
        - list of filtered, scraped urls.
        """
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
        while len(images) < num:
            print(len(images))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            images = driver.find_elements(By.TAG_NAME, "img")

        urls = [image.get_attribute("src") for image in images]
        clean_urls = self._filter_urls(urls, hq=hq)

        return clean_urls
    

    def _download_images(self, urls: list[str]) -> None:
        """
        Downloads the images from the urls.

        Args:
        - urls: list of urls to be downloaded.

        Returns: None
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        for idx, url in enumerate(urls):
            print(url)
            try:
                response = requests.get(url, headers=headers)
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    print("DOWNLOAD ERROR:", e)
                with open(self.output + str(idx+1) + ".jpg", "wb") as file:
                    file.write(response.content)
            except Exception as e:
                print(":C", e)


    def _filter_urls(self, urls: list[str], hq: bool = True) -> list[str]:
        """
        Filters the urls to skip icons and other non-image urls.

        Args:
        - urls: list of urls to be filtered.
        - hq: if True, returns only high quality images urls.

        Returns:
        - list of filtered urls.
        """
        urls = list(filter(lambda u: "/photos/" in u, urls))
        if hq:  
            return list(map(lambda u: u.split("?auto")[0], urls))
        return urls
    

    def set_output(self, path: str) -> None:
        self.output = path
        
        

start = dt.datetime.now()
scr = ScraperV2("F:/Desktop/images/fat_w/")
scr.run("obese woman", 1000, hq=False)
scr.set_output("F:/Desktop/images/fat_m/")
scr.run("obese man", 1000, hq=False)
print("EXECUTION TIME:", dt.datetime.now() - start)
