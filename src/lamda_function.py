import json
from http import HTTPStatus

from calculateAnds import calculateAnds
from responseHanlder import responseHandler

def lambda_handler(event, context):
   
    r = {}
    resStatus = HTTPStatus.OK
    answer = 0
    
    try:
        if "queryStringParameters" not in event:
            resStatus = HTTPStatus.BAD_REQUEST
        else:
            x = event["queryStringParameters"]["text"]
    except:
        print("Not Found")
        resStatus = HTTPStatus.NOT_FOUND
    try:
        answer = calculateAnds(x)
    except:
        print("Bad Request")
        resStatus = HTTPStatus.BAD_REQUEST
    
    r = responseHandler(resStatus, answer)

    reply = json.dumps(r)

    return reply
