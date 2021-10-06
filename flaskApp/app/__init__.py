from flask					import Flask
#from models                 import *

app = Flask(__name__)

#   IF USING FLASK SQL
#database = 'mysql+pymysql://username:password@endpoint/schema'
#app.config['SQLALCHEMY_DATABASE_URI'] = database
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db.init_app(app)


from .routes import *