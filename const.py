import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


OPEN_API_KEY: str = os.getenv('OPEN_API_KEY')
