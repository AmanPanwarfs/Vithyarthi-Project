import unittest
import tempfile
from pathlib import Path

from modules.recommendation import get_recommendations


class StudyPilotLogicTests(unittest.TestCase):

    def test_recommendation_function_returns_list(self):
        result = get_recommendations()
        self.assertIsInstance(result, list)

    def test_project_structure(self):
        root = Path(__file__).resolve().parent.parent
        self.assertTrue((root / "main.py").exists())
        self.assertTrue((root / "modules").exists())
        self.assertTrue((root / "data").exists())


if __name__ == "__main__":
    unittest.main()
