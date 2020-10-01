from flask import request
import json
import sys
from project.controllers import Video


def configure_routes(app, app_cache):

    @app.route('/')
    @app_cache.cached()
    def hello_world():
        return 'Hello, World! ' + app.config['ENV_NAME']

    @app.route('/post/test', methods=['POST'])
    #@app_cache.cached(timeout=10)
    def receive_post():
        headers = request.headers

        auth_token = headers.get('authorization-sha256')
        if not auth_token:
            return 'Unauthorized', 401

        data_string = request.get_data()
        data = json.loads(data_string)
        # sys.stderr.write(f"post data string: {data_string}")    
        request_id = data.get('request_id')
        payload = data.get('payload')
        # sys.stderr.write(f"request id: {request_id} payload: {payload}")    

        if request_id and payload:
            return 'Ok', 200
        else:
            return 'Bad Request', 400

def configure_api_routes(api):
    # Register the resource
    api.add_resource(Video, "/video/<int:video_id>")

