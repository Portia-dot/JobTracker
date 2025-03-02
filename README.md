# Job Tracker

## Overview

Job Tracker is a web scraper that extracts job listings from Google Jobs using Selenium. It retrieves job titles, company names, locations, posting dates, salaries, and job types, and will later store the data in an SQLite database.

## Features

- Scrapes job listings from Google Jobs.
- Supports filtering by job posting time (e.g., today, last 3 days, last month).
- Implements dynamic loading by scrolling to load more job listings.
- Saves results in a structured format.
- Future update: Store job data in SQLite.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (Ensure the version matches your Chrome browser)

### Install Dependencies

Clone this repository and navigate into the project folder:

```bash
git clone https://github.com/Portia-dot/JobTracker.git
cd JobTracker
```

Install required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Scraper

To run the job scraper:

```bash
python main.py
```

### Example Usage

In `main.py`, you can customize the job search parameters:

```python
if __name__ == "__main__":
    scraper = Scraper()
    jobs = scraper.searchGoogleJobs("Data Scientist", "Canada", maxResults=50, timeFilter="d")
    scraper.closeDriver()
```

This will scrape up to 50 job listings for **Data Scientist** positions in **Canada**, filtering only jobs posted **today (**\`\`**)**.


