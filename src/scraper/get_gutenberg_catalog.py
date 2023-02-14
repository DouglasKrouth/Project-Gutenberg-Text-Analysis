# We want to find a copy of gutenberg_index.csv if it exists?
# Author : Douglas Krouth
import pathlib
import yaml
import os
import requests
import logging
from config import Config

cfg = Config()


def get_gutenberg_index(refresh_index=False):
    """
    Util function to get the catalog data. If the file exists in ../data/ use it, else check glob, else download the file
    """
    # "Force refresh" by param
    if refresh_index:
        _download_gutenberg_index()
        return
    # Check the data directory for file first
    if os.path.isfile(r"../data/gutenberg_index.csv"):
        print("found file")
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
    Private util to fetch the Gutenberg catalob if it is not present in ../data or on local machine
    """
    # "https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv"
    url = cfg.config_params["gutenberg_index_link"]
    try:
        r = requests.get(url)
        logging.info("Request successful")
    # If the request fails, throw an exception
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # Write the contents from the requests to csv file
    open("../data/gutenberg_index.csv", "wb").write(r.content)
