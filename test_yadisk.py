import unittest
from YaDisk import YaUploader
import requests
from data import token

class TestYaDisk(unittest.TestCase):
    def setUp(self):
        print("method setUp")   
    def tearDown(self):
        print("method tearDown")   
    def test_create_folder(self):
        # На основе документации при успешном создании папки код 201, проверем на это
        connection = YaUploader(token)
        dir_name = 'Test_folder'
        result = connection.create_folder(dir_name)
        connection.delete_folder(dir_name)
        self.assertEqual(result.status_code, 201)

    def test_name_folder(self):
        connection = YaUploader(token)  
        dir_name = 'Test_folder'
        connection.create_folder(dir_name)
        result = connection.return_meta(dir_name)
        connection.delete_folder(dir_name)
        self.assertEqual(result.json()['name'], dir_name)

if __name__ == '__main__':
    unittest.main()


# КАКИЕ МОГУТ БЫТЬ ОТРИЦАТЕЛЬНЫЕ ТЕСТЫ В ДАННОМ СЛУЧАЕ? 