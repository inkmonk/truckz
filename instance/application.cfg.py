SERVER_NAME = "localhost:5000"

DEBUG = True
ASSETS_DEBUG = True

DB_USERNAME = 'admin'
DB_PASSWORD = 'admin'
DB_SERVER = 'localhost'
DB_NAME = 'truckz'

SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{passwd}@{server}/{db}'.format(
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    server=DB_SERVER,
    db=DB_NAME)


SECRET_KEY = 'd493a55fabdb4d5895879fb1ed1fbe12'
SECRET_KEY_HASH = ''

SECURITY_PASSWORD_HASH = "bcrypt"
SECURITY_PASSWORD_SALT = "c751851023e64daaa5c1197edaa20f42"