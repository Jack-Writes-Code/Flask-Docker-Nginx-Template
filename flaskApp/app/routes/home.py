from flask					import jsonify, request, redirect, render_template
from app                    import app#, db

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', pageTitle="Home")