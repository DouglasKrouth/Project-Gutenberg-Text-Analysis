# We want to find a copy of gutenberg_index.csv if it exists?
# Author : Douglas Krouth
import pathlib
import yaml
import os
import requests
import logging
from config import Config

cfg = Config()
logging.getLogger()


def get_gutenberg_index(refresh_index=False):
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
        _download_gutenberg_index()
        return
    # Check the data directory for file first
    if os.path.isfile(r"../data/gutenberg_index.csv"):
        logging.info("found file")
        return
    # If file not found in ../data, check with pathlib across homedir (slow)
    else:
        search = sorted(pathlib.Path("/home").glob("**/gutenberg_index.csv"))
        if search is not None:
            for i in search:
                print(i)
        # If file is not found from ~/, download from gutenberg.org
        else:
            _download_gutenberg_index()


def _download_gutenberg_index():
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
    open("../data/gutenberg_index.csv", "wb").write(r.content)
