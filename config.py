class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/library_db'
    DEBUG = True

class TestingConfig:
    pass

class ProductionConfig:
    pass
