# isaExplorer

[![Build Status](https://travis-ci.org/phenomecentre/isaExplorer.svg?branch=master)](https://travis-ci.org/phenomecentre/isaExplorer) [![codecov](https://codecov.io/gh/phenomecentre/isaExplorer/branch/master/graph/badge.svg)](https://codecov.io/gh/phenomecentre/isaExplorer) ![Python36](https://img.shields.io/badge/python-3.6-blue.svg) [![PyPI](https://img.shields.io/pypi/v/isaExplorer.svg)](https://pypi.org/project/isaExplorer/)

Tools for exploring ISA-format study descriptions

To Install `isaExplorer` from github, you can do:

  `pip install isaExplorer`

And then you can import it in your Python code as follows:

  `import isaExplorer as ie`

and then use the available functions such as this function which lists the Studies and Assays in an ISA archive:

  `ie.exploreISA('/path/to/ISATAB/')`

or this function which returns a specific Assay from a specific Study:

  `first_assay = ie.getISAAssay(1, 1, '/path/to/ISATAB/')`
