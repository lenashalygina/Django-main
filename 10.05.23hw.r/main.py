from flask import Flask
from flask import jsonify
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from werkzeug.serving import run_simple

app_flask = Flask(__name__)

@app_flask.route('/flask')
def flask_endpoint():
    return jsonify(message='Hello from Flask!')


django_app = get_wsgi_application()

def django_endpoint(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [b'{"message": "Hello from Django!"}']


app_fastapi = FastAPI()

@app_fastapi.get('/fastapi')
def fastapi_endpoint():
    return {'message': 'Hello from FastAPI!'}

# Run the application
if __name__ == '__main__':
    run_simple('localhost', 5000, app_flask)
    run_simple('localhost', 8000, django_app)
    uvicorn.run(app_fastapi, host='localhost', port=3000)
