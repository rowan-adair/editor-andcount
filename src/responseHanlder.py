from http import HTTPStatus

def responseHandler(resStatus, answer):
        message400 = "Error: you must provide a 'text' parameter."
        if resStatus == HTTPStatus.OK:
            return {
                "status": HTTPStatus.OK,
                "error": False,
                "data": {
                    "result": "The number of ands is: " + str(answer),
                    "total": answer
                },
                "message": HTTPStatus.OK.phrase,
            }
        if resStatus ==  HTTPStatus.INTERNAL_SERVER_ERROR:
                return {
                "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                "error": True,
                "message": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
            }
        if resStatus ==  HTTPStatus.BAD_REQUEST:
            return {
                "status": HTTPStatus.BAD_REQUEST,
                "error": True,
                "message": HTTPStatus.BAD_REQUEST.phrase + " " + message400
            }
        if resStatus ==  HTTPStatus.NOT_FOUND:
            return {
                "status": HTTPStatus.NOT_FOUND,
                "error": True,
                "message": HTTPStatus.NOT_FOUND.phrase,
            }