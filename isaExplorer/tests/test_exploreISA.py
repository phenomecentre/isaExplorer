from unittest import TestCase
import os

import isaExplorer

class TestExploreISA(TestCase):
    def test_exploreISA(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')
        self.assertIsNone(isaExplorer.exploreISA(pathToISATABFile, verbose=False))

class TestGetISAAssay(TestCase):
    def test_getISAAssay(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')
        self.assertTrue(isaExplorer.isaExplorer.getISAAssay(1,1,pathToISATABFile))

class TestGetISAStudy(TestCase):
    def test_getISAStudy(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')
        self.assertTrue(isaExplorer.isaExplorer.getISAStudy(1,pathToISATABFile))

class TestAppendStudytoISA(TestCase):
    def test_AppendStudytoISA(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')
        study = isaExplorer.isaExplorer.getISAStudy(1,pathToISATABFile)
        self.assertIsNone(isaExplorer.isaExplorer.appendStudytoISA(study,pathToISATABFile))

class TestDropStudyFromISA(TestCase):
    def test_dropStudyFromISA(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')
        self.assertIsNone(isaExplorer.isaExplorer.dropStudyFromISA(2,pathToISATABFile))

class TestAppendAssayToStudy(TestCase):
    def test_appendAssayToStudy(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')
        assay = isaExplorer.isaExplorer.getISAAssay(1,1,pathToISATABFile)
        self.assertIsNone(isaExplorer.isaExplorer.appendAssayToStudy(assay,1,pathToISATABFile))

class TestDropAssayFromStudy(TestCase):
    def test_dropAssayFromStudy(self):
        pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')
        self.assertIsNone(isaExplorer.isaExplorer.dropAssayFromStudy(2,1,pathToISATABFile))
