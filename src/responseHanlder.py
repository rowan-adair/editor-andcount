from http import HTTPStatus

def responseHandler(resStatus, answer):
        message400 = "Error: you must provide a 'text' parameter."
        match resStatus:
            case HTTPStatus.OK:
                return {
                    "status": HTTPStatus.OK,
                    "error": False,
                    "data": {
                        "result": "The average length of words in text is: " + str(answer),
                        "total": answer
                    },
                    "message": HTTPStatus.OK.phrase,
            }
            case HTTPStatus.INTERNAL_SERVER_ERROR:
                return {
                    "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                    "error": True,
                    "message": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
                }
            case HTTPStatus.BAD_REQUEST:
                return {
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": True,
                    "message": HTTPStatus.BAD_REQUEST.phrase + " " + message400
                }
            case HTTPStatus.NOT_FOUND:
                return {
                    "status": HTTPStatus.NOT_FOUND,
                    "error": True,
                    "message": HTTPStatus.NOT_FOUND.phrase,
                }