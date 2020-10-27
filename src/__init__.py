from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config['SECRET_KEY'] = '$2b$12$gw7YsCOzeX3yJQIS24wOc.8khKFM/0Ce2eVdB90Zx3ZViHrkoq7pG'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'info'

from src import routes
from src.models import User

