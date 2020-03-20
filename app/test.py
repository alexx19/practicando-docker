import unittest
import usercontroller


class TestDockerapp(unittest.TestCase):

    def setUp(self):
        self.usercontroller = usercontroller.app.test_client()

    def test_save_value(self):
        response = self.usercontroller.post('/', data=dict(submit='save', key='2', cache_value='two'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data

    def test_load_value(self):
        self.usercontroller.post('/', data=dict(submit='save', key='2', cache_value='two'))
        response = self.usercontroller.post('/', data=dict(submit='load', key='2'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data


if __name__=='__main__':
    unittest.main()
