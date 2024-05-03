import unittest
import json
from base64 import b64encode

from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        
    def test_a_new_process_actor(self):
        data = {
            "id": "0968599020001",
            "isActor": True
        }
        response = self.app.post('/api/v1/new_process', json=data, headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)
        
    def test_b_new_process_infractor(self):
        data = {
            "id": "0968599020001",
            "isActor": False
        }
        response = self.app.post('/api/v1/new_process', json=data, headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)
    
    def test_get_process_actor(self):
        response = self.app.get('/api/v1/existing_process/0968599020001/actor', headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)
        

    def test_get_process_infractor(self):
        response = self.app.get('/api/v1/existing_process/0968599020001/infractor', headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)
        

    def get_auth_header(self):
        return {'Authorization': 'Basic {}'.format(
            b64encode(b"username:password").decode('utf-8'))}

if __name__ == '__main__':
    unittest.main()
