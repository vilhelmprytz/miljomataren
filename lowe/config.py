from os import environ

# basic app
BASE_URL = environ.get("BASE_URL", "http://localhost:5000")
FRONTEND_URL = environ.get("FRONTEND_URL", "http://localhost:3000")

# database credentials
DATABASE_USERNAME = environ.get("DATABASE_USERNAME", "miljomataren")
DATABASE_NAME = environ.get("DATABASE_NAME", "miljomataren")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD", "password")
DATABASE_HOST = environ.get("DATABASE_HOST", "127.0.0.1")

# redis (optional)
REDIS_HOST = environ.get("REDIS_HOST", "localhost")

# google authentication
GOOGLE_CLIENT_ID = environ["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = environ["GOOGLE_CLIENT_SECRET"]

# insecure CORS
INSECURE_CORS = environ.get("INSECURE_CORS", False)
