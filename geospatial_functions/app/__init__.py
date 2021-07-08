# Imports from Flask
from flask import Flask, render_template, send_from_directory, flash, abort, url_for, redirect

# Extension for implementing Alembic database migrations
# from flask_migrate import Migrate

# Extension for implementing SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy import text

import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=os.getenv('SQL_DB_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
#    MAX_CONTENT_LENGTH=16*1024*1024,
#    IMAGE_UPLOADS=os.path.join(basedir, "uploads"),
#    ALLOWED_IMAGE_EXTENSIONS=["jpeg", "jpg", "png"]
)

# Initializing extensions
db = SQLAlchemy(app)

# Imports from subpackages (views)
# from app.album import views
# from app.main import views
