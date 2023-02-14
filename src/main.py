import config
from scraper import get_gutenberg_catalog

def main():
    print("running main")
    get_gutenberg_catalog.get_gutenberg_index()
    

if __name__ == "__main__":
    main()