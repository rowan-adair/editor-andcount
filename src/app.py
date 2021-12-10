from flask import Flask
from flask import request
from flask import Response
from http import HTTPStatus

from calculateAnds import calculateAnds
from responseHanlder import responseHandler

import json

app = Flask(__name__)

@app.route('/')
def handleGet():
    r = {}
    resStatus = HTTPStatus.OK
    answer = 0
    
    try:
        x = str(request.args.get('text'))
    except:
        print("Not Found")
        resStatus = HTTPStatus.NOT_FOUND
    try:
        answer = calculateAnds(x)
    except:
        print("Internal Server Error")
        resStatus = HTTPStatus.INTERNAL_SERVER_ERROR
    
    r = responseHandler(resStatus, answer)

    reply = json.dumps(r)

    response = Response(response=reply, status=resStatus, mimetype="application/json")
    response.headers['Content-Type']="application/json"
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
