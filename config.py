from dotenv import load_dotenv
import os

env = load_dotenv()

sender = os.getenv('SENDER')
password = os.getenv('PASSWORD')
