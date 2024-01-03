import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.scanner import fetch_url_content


class TestScannerFunctions(unittest.TestCase):

    def test_fetch_url_content(self):
        url = "https://example.com"
        content = fetch_url_content(url)
        self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main()
