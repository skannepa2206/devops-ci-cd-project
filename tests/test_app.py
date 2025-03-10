import unittest
import requests
import time
import sys


class TestApp(unittest.TestCase):
    def setUp(self):
        # Give the app a moment to fully start
        time.sleep(2)
        self.base_url = "http://localhost:5000"

    def test_home_endpoint(self):
        try:
            print(f"Testing connection to {self.base_url}")
            response = requests.get(f"{self.base_url}")
            print(f"Response status: {response.status_code}")
            print(f"Response text: {response.text}")
            self.assertEqual(response.status_code, 200)
            self.assertIn("DevOps Automation", response.text)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            self.fail("Could not connect to the application - deployment may have failed")


if __name__ == "__main__":
    unittest.main()