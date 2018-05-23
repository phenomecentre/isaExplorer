from unittest import TestCase
import os
import tempfile
from distutils import dir_util

import isaExplorer

pathToISATABFile = os.path.join(os.path.dirname(__file__), 'test_data', 'MTBLS1')

class TestExploreISA(TestCase):
    def test_exploreISA(self):
        self.assertIsNone(isaExplorer.exploreISA(pathToISATABFile, verbose=False))

class TestGetISAAssay(TestCase):
    def test_getISAAssay(self):
        self.assertTrue(isaExplorer.isaExplorer.getISAAssay(1,1,pathToISATABFile))

class TestGetISAStudy(TestCase):
    def test_getISAStudy(self):
        self.assertTrue(isaExplorer.isaExplorer.getISAStudy(1,pathToISATABFile))

class Test_study_operations(TestCase):
    def test_AppendStudytoISA(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            pathToTempISATABFile = os.path.join(tmpdirname, 'MTBLS1')
            dir_util.copy_tree(pathToISATABFile, pathToTempISATABFile)

            study = isaExplorer.isaExplorer.getISAStudy(1,pathToTempISATABFile)
            self.assertIsNone(isaExplorer.isaExplorer.appendStudytoISA(study,pathToTempISATABFile))

    def test_dropStudyFromISA(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            pathToTempISATABFile = os.path.join(tmpdirname, 'MTBLS1')
            dir_util.copy_tree(pathToISATABFile, pathToTempISATABFile)

            study = isaExplorer.isaExplorer.getISAStudy(1,pathToTempISATABFile)
            isaExplorer.isaExplorer.appendStudytoISA(study,pathToTempISATABFile)

            self.assertIsNone(isaExplorer.isaExplorer.dropStudyFromISA(2,pathToTempISATABFile))

class Test_assay_operations(TestCase):
    def test_appendAssayToStudy(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            pathToTempISATABFile = os.path.join(tmpdirname, 'MTBLS1')
            dir_util.copy_tree(pathToISATABFile, pathToTempISATABFile)

            assay = isaExplorer.isaExplorer.getISAAssay(1,1,pathToTempISATABFile)
            self.assertIsNone(isaExplorer.isaExplorer.appendAssayToStudy(assay,1,pathToTempISATABFile))

    def test_dropAssayFromStudy(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            pathToTempISATABFile = os.path.join(tmpdirname, 'MTBLS1')
            dir_util.copy_tree(pathToISATABFile, pathToTempISATABFile)

            assay = isaExplorer.isaExplorer.getISAAssay(1,1,pathToTempISATABFile)
            isaExplorer.isaExplorer.appendAssayToStudy(assay,1,pathToTempISATABFile)

            self.assertIsNone(isaExplorer.isaExplorer.dropAssayFromStudy(2,1,pathToTempISATABFile))
