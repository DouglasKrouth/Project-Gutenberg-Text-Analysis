# Grab a book! This module will be used to retrieve a book from the PG website.
# To avoid hitting their site more than required, we'll cache the book locally once it's retrieved unless specified not to do so.
# Author : Douglas Krouth
import pathlib
import yaml
import os
import requests
import logging
from config import Config

cfg = Config()
logging.getLogger()

