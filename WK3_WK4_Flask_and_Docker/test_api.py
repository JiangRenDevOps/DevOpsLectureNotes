import unittest

from WK3_WK4_Flask_and_Docker.app import app


class TestApi(unittest.TestCase):
    """Test case for the client methods."""
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_hello_world(self):
        res = self.app.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, b"Hello World!")

    def test_post_my_info_should_return_201_when_json_is_valid(self):
        res = self.app.post("/post_my_info", json={"name": "Yu", "age": 18})
        self.assertEqual(res.status_code, 201)

    def test_post_my_info_should_return_404_when_json_is_invalid(self):
        res = self.app.post("/post_my_info", json={"na": "Yu", "ag": 18})
        self.assertEqual(res.status_code, 404)