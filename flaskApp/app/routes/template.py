from flask					import jsonify, request, redirect
from app                    import app#, db

@app.route('/template', methods=['GET'])
def template_route():
    return jsonify({"Success":"True"})