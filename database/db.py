# Database Configuration
# Imports
from flask_mongoengine import MongoEngine

# Create db object
db = MongoEngine()

# Host
host = 'mongodb://localhost/petservs_mbd'


# initialize_db method
def initialize_db(app):
    db.init_app(app)