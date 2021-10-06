from flask					import Flask
#from models                 import *

app = Flask(__name__)

#   IF USING FLASK SQL
#database = 'mysql+pymysql://dbmasteruser:4{O-r<_BhvF9TfR$:#IrBkIFCH1_>B]P@ls-b5edb0a67e56a7f37b94c35ce292601ca7cadec8.cvasw40kycww.eu-west-2.rds.amazonaws.com/dbmaster'
#app.config['SQLALCHEMY_DATABASE_URI'] = database
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db.init_app(app)


from .routes import *