from http import HTTPStatus
import unittest
import app
from flask import Flask
import calculateAnds

app = Flask(__name__)

class TestAverage(unittest.TestCase):
    
    def setup(self): 
          app.app.config['TESTING'] = True 
          self.app = app.app.test_client() 
    
    def test_average(self):
        self.assertEqual(calculateAnds.calculateAnds('and'), 1)

    def test_average_empty_string(self):
        self.assertEqual(calculateAnds.calculateAnds(''), 0)

    def test_api_call(self):
        client = app.test_client()
        try:
            response = client.get("http://0.0.0.0:5001/?text=and")
            assert response.status_code == 200
            assert response.json == {
                    "status": HTTPStatus.OK,
                    "error": False,
                    "data": {
                        "result": "The number of ands is: " + 1,
                        "total": 1
                    },
                    "message":  HTTPStatus.OK,
                }
        except:
            return 'Something went wrong when calling api' 
    
    def test_api_call_400(self):
        client = app.test_client()
        message400 = "Error: you must provide a 'text' parameter."
        try:
            response = client.get("http://0.0.0.0:5001/")
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
