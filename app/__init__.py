from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = '7f1b71988d6021d7445f2bd7a8fd192e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense.db'  # Example DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids warning


# Initialize database with the app
db = SQLAlchemy(app)

from app import models  # ✅ Import models at the end to avoid circular imports

if not os.path.exists('expense.db'):
    with app.app_context():
        db.create_all()
        print('Database created!')

# Import routes at the end to avoid circular imports
from app import routes  # ✅ Correct

