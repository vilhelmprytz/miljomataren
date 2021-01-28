from os import environ

# database credentials
DATABASE_USERNAME = environ.get("DATABASE_USERNAME", "miljomataren")
DATABASE_NAME = environ.get("DATABASE_NAME", "miljomataren")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD", "password")
DATABASE_HOST = environ.get("DATABASE_HOST", "127.0.0.1")

# google authentication
GOOGLE_CLIENT_ID = environ["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = environ["GOOGLE_CLIENT_SECRET"]
