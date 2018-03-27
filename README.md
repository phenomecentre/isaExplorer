# isaExplorer
Tools for exploring ISA-format study descriptions

To Install `isaExplorer` from github, you can do:

`pip install git+git://github.com/phenomecentre/isaexplorer.git`

And then you can import it in your Python code as follows:

`import isaExplorer as ie`
and then use the available functions such as this function which lists the Studies and Assays in an ISA archive:
`ie.exploreISA('/path/to/ISATAB/')`

or this function which returns a specific Assay from a specific Study:

`first_assay = ie.getISAAssay(1, 1, '/path/to/ISATAB/')`
