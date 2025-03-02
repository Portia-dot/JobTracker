from scraper import Scraper
if __name__ == "__main__":
    scraper = Scraper()
    jobs = scraper.searchGoogleJobs("Data Scientist", 'Canada', maxResults = 100, timeFilter = "d")
    scraper.closeDriver()

