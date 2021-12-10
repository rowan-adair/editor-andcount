from http import HTTPStatus
import unittest
import app
from flask import Flask
import calculateAverage

app = Flask(__name__)

class TestAverage(unittest.TestCase):
    
    def setup(self): 
          app.app.config['TESTING'] = True 
          self.app = app.app.test_client() 
    
    def test_average(self):
        self.assertEqual(calculateAverage.averageWordLength('silly billy'), 5)

    def test_average_empty_string(self):
        self.assertEqual(calculateAverage.averageWordLength(''), 0)

    def test_api_call(self):
        client = app.test_client()
        try:
            response = client.get("http://0.0.0.0:5000/?text=foo")
            assert response.status_code == 200
            assert response.json == {
                    "status": HTTPStatus.OK,
                    "error": False,
                    "data": {
                        "result": "The average length of words in text is: " + 3,
                        "total": 3
                    },
                    "message":  HTTPStatus.OK,
                }
        except:
            return 'Something went wrong when calling api' 
    
    def test_api_call_400(self):
        client = app.test_client()
        message400 = "Error: you must provide a 'text' parameter."
        try:
            response = client.get("http://0.0.0.0:5000/")
            assert response.status_code == 400
            assert response.json == {
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": True,
                    "message":  HTTPStatus.BAD_REQUEST.phrase + " " + message400,
                }
        except:
            return 'Something went wrong when calling api' 

if __name__ == 'main':
    unittest.main()
