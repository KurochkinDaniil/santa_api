from environs import Env

env = Env()
env.read_env()

FAST_API_APP_HOST = env.str("FAST_API_APP_HOST")
FAST_API_APP_PORT = env.int("FAST_API_APP_PORT")
CORS_ORIGINS = env.list("CORS_ORIGINS")

DB_ENGINE = env.str("DB_ENGINE")
DB_PORT = env.str("DB_PORT")
DB_HOST = env.str("DB_HOST")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_NAME = env.str("DB_NAME")
DB_USER = env.str("DB_USER")
