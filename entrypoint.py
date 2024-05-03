from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
from dotenv import load_dotenv
from flask import abort

import os

from src.utils.files import load_file
from src.scrapping.scrapping import get_page_info

load_dotenv()

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

app.config['BASIC_AUTH_USERNAME'] = os.getenv("BASIC_AUTH_USERNAME")
app.config['BASIC_AUTH_PASSWORD'] = os.getenv("BASIC_AUTH_PASSWORD")
url_page_scrap = os.getenv("URL_PAGE_SCRAP")
chrome_driver_local_path = os.getenv("CHROME_DRIVER_LOCAL_PATH")

basic_auth = BasicAuth(app)


# Proceso existente para actores
@app.route('/api/v1/existing_process/<id>/actor', methods=['GET'])
@basic_auth.required
def get_process_actor(id):
    file_path = "./src/json/" + id + "_actor.json"
    result = load_file(file_path)
    return result

# Proceso existente para infractores
@app.route('/api/v1/existing_process/<id>/infractor', methods=['GET'])
@basic_auth.required
def get_process_infractor(id):
        file_path = "./src/json/" + id + "_infractor.json"
        result = load_file(file_path)
        return result


@app.route('/api/v1/new_process', methods=['POST'])
@basic_auth.required
def new_process():
    
    if 'id' not in request.json:
        error_response = {"error": "id is required"}
        return jsonify(error_response), 400
        
    id = request.json["id"]

    if 'isActor' not in request.json:
        error_response = {"error": "isActor is required"}
        return jsonify(error_response), 400

    isActor = request.json["isActor"]

    response = {"id": id, "isActor": isActor}
    
    if not isinstance(isActor, bool):
        error_response = {"error": "isActor is boolean value"}
        return jsonify(error_response), 400

    get_page_info(id, url_page_scrap, isActor, chrome_driver_local_path, True)
    
    actor = "_infractor.json"
    if isActor:
        actor = "_actor.json"
        
    
    file_path = "./src/json/" + id + actor
    result = load_file(file_path)
    
    return result

# Mostar documento del proceso
@app.route('/api/v1/document/<document_id>', methods=['GET'])
@basic_auth.required
def get_document(id):
    process_id = id
    response = {"document": process_id}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


