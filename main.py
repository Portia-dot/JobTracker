from scraper import Scraper
from database import Database
if __name__ == "__main__":
    scraper = Scraper()
    database = Database()

    jobs = scraper.searchGoogleJobs("Data Scientist", 'Canada', maxResults = 10, timeFilter = "d")

    #Save Each Job
    for job in jobs:
        database.insertJob(job)


    #Fetch and Print Jobs
    storeJob = database.fetchJobs()
    for job in storeJob:
        print(job)
#Close browser and Database
    database.close()
    scraper.closeDriver()

