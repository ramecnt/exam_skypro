class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@pg/db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    JSON_AS_ASCII = False
