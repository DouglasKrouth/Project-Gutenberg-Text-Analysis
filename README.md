# Notes on Gutenberg scraping.
We don't want to scrape Project Gutenberg's site using automations like Selenium or Puppeteer as they have explicitly stated not to. The main concern presented in their "robots.txt" and requests warnings states that we can't use their website's search functionality to obtain the index of a given book. To work around this, we want to grab a copy of the Project Gutenberg catalog (referenced as *gutenberg_index.csv*) and perform our search on this registry prior to making a request to the PG website. The goal of this is to know in advance which record/book ID we want and only send a request for this specific value(s).</br>

To implement our search functionality on a local scale, we'll do the following:
1. Request a copy of the catalog from Project Gutenberg [download_link](https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv)
2. Create a dictionary/hashmap that links a book title to the PG book index/lookup value.
    - Fun idea : Cache these results to speed up search? For a project of this scale it won't likely be necessary, but it's a fun challenge!
3. Request the specific book from PG in html format.
4. Process the html response with BeautifulSoup, etc.

# TODO list
1. Add a Makefile to configure data directory, fetch dependencies


# Project Gutenberg Text Analysis
- Testing functionality of Spacy, NLTK.
- Includes methods to poll Gutenberg for source directory, caching results if desired
- TODO : CLI implementation