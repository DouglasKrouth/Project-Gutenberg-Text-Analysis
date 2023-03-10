# We want to find a copy of gutenberg_index.csv if it exists, load it into ../data directory
# Author : Douglas Krouth
import pathlib
import yaml
import os
import requests
import logging
import pandas as pd
import time
from config import Config

cfg = Config()
logging.getLogger()


def _get_gutenberg_catalog(refresh_index=False):
    """
    Util function to get the catalog data. If the file exists in ../data/ use it, else check glob, else download the file.
    - Condition to download file if specified : If config param use_cache_catalog == False and refresh_index == True, then download the catalog from scratch from Gutenberg
    """
    # Check if config contains use_cache_catalog value
    if "use_cache_catalog" in cfg.config_params.keys():
        use_cache_catalog = cfg.config_params["use_cache_catalog"]
    else:
        use_cache_catalog = None
    # "Force refresh" by param or if cfg use_cache param is set to False
    if refresh_index and not use_cache_catalog:
        _download_gutenberg_catalog()
        return
    # Check the data directory for file first
    if os.path.isfile(r"../data/gutenberg_index.csv"):
        logging.info("found file")
        return
    else:
        _download_gutenberg_catalog()


def _download_gutenberg_catalog():
    """
    Private util to fetch the Gutenberg catalog if it is not present in ../data or on local machine
    """
    # Check if a new url, for some reason?, was passed into config for pg_catalog
    # "https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv"
    if "gutenberg_index_link" in cfg.config_params.keys():
        url = cfg.config_params["gutenberg_index_link"]
    else:
        url = "https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv"

    try:
        r = requests.get(url)
        logging.info(
            "Request to Project Gutenberg successful. pg_catalog.csv retrieved."
        )
    # If the request fails, throw an exception
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # Write the contents from the requests to csv file
    os.makedirs(r"../data", exist_ok=True)
    open("../data/gutenberg_index.csv", "wb").write(r.content)


def load_catalog(verbose=False):
    """
    External method for loading the PG catalog csv into selected format

    Verbose : Boolean, if True displays head and catalog DataFrame info
    """
    pg_catalog_path = r"../data/gutenberg_index.csv"
    for i in range(0, 3):
        while True:
            try:
                catalog_df = pd.read_csv(
                    pg_catalog_path,
                    dtype={
                        "Text#": int,
                        "Type": str,
                        "Issued": str,
                        "Title": str,
                        "Language": str,
                        "Authors": str,
                        "Subjects": str,
                        "LoCC": str,
                        "Bookshelves": str,
                    },
                )
                if verbose:
                    # Default to False, will clog logs if always output
                    logging.debug(
                        "PG Catalog file cdate : {}".format(
                            time.ctime(os.path.getctime(pg_catalog_path))
                        )
                    )
                    logging.debug(catalog_df.info())
                return catalog_df
            except FileNotFoundError:
                print("Gutenberg catalog not found, downloading!")
                _get_gutenberg_catalog()
                continue
            break
