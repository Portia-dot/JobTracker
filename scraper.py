from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random

class Scraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.119 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)

    def check(self, card):
        if len(card) == 0:
            print(f" No card found.")
            return False
        return True
    def listings(self, className):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, className))
        )
    def scrollToLoad(self, maxResult):
        lastHeight = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2,10))
            jobCard = self.driver.find_elements(By.CLASS_NAME, "GoEOPd")
            if len(jobCard) >= maxResult:
                break
            newHeight = self.driver.execute_script("return document.body.scrollHeight")
            if newHeight == lastHeight:
                break
            lastHeight = newHeight


    def searchGoogleJobs(self, query, location, maxResults = 100, timeFilter = ""):
        baseUrl = f"https://www.google.com/search?q={query}+jobs+in+{location}&udm=8"
        searchUrl =  f"{baseUrl}&tbs=qdr:={timeFilter}" if timeFilter else baseUrl
        self.driver.get(searchUrl)
        time.sleep(random.uniform(3, 6))
        self.scrollToLoad(maxResults)
        # driver.save_screenshot("google-jobs-" + query + ".png")

        jobs = []
        #Dectect Jobs
        try:
            self.listings("gmxZue")
            # Locate job listing
            jobCard = self.driver.find_elements(By.CLASS_NAME, "GoEOPd")
            detailCard = self.driver.find_elements(By.CLASS_NAME, "ApHyTb.ncqQR")

            if not self.check(jobCard) and not self.check(detailCard):
                return []

            totalJobs = min(len(jobCard), len(detailCard), maxResults)
            for i in range(totalJobs):
                card = jobCard[i]
                detail = detailCard[i]
                try:
                    title = card.find_element(By.CLASS_NAME, "tNxQIb").text
                except:
                    title = "N/A"
                #Company Name
                try:
                    companyName = card.find_element(By.CSS_SELECTOR, ".wHYlTd.MKCbgd.a3jPc").text
                except:
                    companyName = "N/A"
                #Location
                try:
                    location = card.find_element(By.CLASS_NAME, "wHYlTd.FqK3wc").text
                except:
                    location = "N/A"
                try:
                    timePosted = detail.find_element(By.XPATH, ".//span[@class='Yf9oye' and starts-with(@aria-label, 'Posted')]").get_attribute("aria-label")
                except:
                    timePosted = "N/A"
                #Salary
                try:
                    salary = detail.find_element(By.XPATH, ".//span[@class='Yf9oye' and starts-with(@aria-label, 'Salary')]").get_attribute("aria-label")
                except:
                    salary = "N/A"
                #Employment type

                try:
                    jobType = detail.find_element(By.XPATH, ".//span[@class='Yf9oye' and starts-with(@aria-label, 'Employment Type')]").get_attribute("aria-label")
                except:
                    jobType = "N/A"

            #Storing Result into a dictionary with keys

                jobEntry = {
                    "title": title,
                    "companyName": companyName,
                    "location": location,
                    "timePosted": timePosted,
                    "salary": salary,
                    "jobType": jobType,
                }
                jobs.append(jobEntry)
        except Exception as e:
            print(e)
            print("No results found.")
        return jobs
    def closeDriver(self):
        self.driver.close()
        self.driver.quit()



