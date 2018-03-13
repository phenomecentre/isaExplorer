from unittest import TestCase
import os

import isaExplorer

class TestExploreISA(TestCase):
    def test_is_string(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), './test_data/BII-I-1/')
        self.assertTrue(isaExplorer.exploreISA(pathToISATABFile, verbose=False))
