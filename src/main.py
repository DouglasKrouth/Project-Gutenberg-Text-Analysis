import config
import logging
import sys

# Project
from scraper import get_gutenberg_catalog

# ---
# LOGGING
# https://stackoverflow.com/a/14058475/11187377
# ---
root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
root.addHandler(handler)


def main():
    logging.info("running main")
    get_gutenberg_catalog.get_gutenberg_index()


if __name__ == "__main__":
    main()
