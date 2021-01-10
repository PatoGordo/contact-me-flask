from flask import Flask, request
from flask_cors import CORS

#internal modules
from src.functions.index import Index
from src.functions.set import setData
from src.functions.get import getData
from src.functions.responses import ResponseMaker

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def index():
  return Index()

@app.route('/set', methods=["POST"])
def set():
  body = request.get_json()

  if("name" not in body or "message" not in body or "email" not in body):
    return ResponseMaker(400, "Message not added! Required field[name, message or email] is empty.")
  
  contact = setData(body["name"], body["message"], body["email"])
  
  return ResponseMaker(200, "Message successfully added!", "contactAdded: ", contact)

@app.route('/get', methods=["GET"])
def get():
  return getData()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)