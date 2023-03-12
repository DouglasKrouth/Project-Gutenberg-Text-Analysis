import fuzzywuzzy
import pandas as pd
import config
import logging
import sys
import os

# Project
from scraper import get_gutenberg_catalog

logging.getLogger()


class Catalog:
    '''
    Reads in the PG catalog file, stores it in a DataFrame and provides some helper functions
    '''
    catalog_path = "../data/gutenberg_index.csv"
    search_threshold = 80

    def __init__(self):
        if os.path.exists(self.catalog_path):
            self.catalog_df = pd.read_csv(self.catalog_path, low_memory=False).sort_values("Title", ascending=False)
            self.titles = self.catalog_df['Title']
        else:
            # PG catalog is not present, download it from their site
            logging.info("Catalog not found in ../data/. Fetching from PG site.")
            get_gutenberg_catalog.get_gutenberg_index()
            self.catalog_df = pd.read_csv(self.catalog_path, low_memory=False).sort_values("Title", ascending=False)
            self.titles = self.catalog_df['Title']

    def search_title(self, book_title):
        first_letter = book_title[0]
        # Grab the slice of the DataFrame which has the first letter of the book title
        df = self.catalog_df[self.catalog_df.Title.str.startswith(first_letter)]
        print(df.shape)