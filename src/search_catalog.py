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
    catalog_path = "../data/gutenberg_index.csv"

    def __init__(self):
        if os.path.exists(self.catalog_path):
            self.catalog_df = pd.read_csv(self.catalog_path)
        else:
            logging.info("Catalog not found in ../data/. Fetching from PG site.")
            get_gutenberg_catalog.get_gutenberg_index()
            self.catalog_df = pd.read_csv(self.catalog_path)
            
    def search(self, book_title):
        pass