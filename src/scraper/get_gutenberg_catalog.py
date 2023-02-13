# We want to find a copy of gutenberg_index.csv if it exists?
import pathlib
import yaml

# Utility function that fetches the Project Gutenberg catalog from their website
def download_gutenberg_index():
    url = r"https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv"
    try:
        r = requests.get(url)
        logging.info("Request successful")
    # If the request fails, throw an exception
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # Write the contents from the requests to csv file
    open("gutenberg_index.csv", "wb").write(r.content)

def get_gutenberg_index(search_for_existing_csv=True):
    search = sorted(pathlib.Path('/home').glob('**/gutenberg_index.csv'))
    if search is not None:
        for i in search:
            print(i)
    else:
        download_gutenberg_index()

get_gutenberg_index()