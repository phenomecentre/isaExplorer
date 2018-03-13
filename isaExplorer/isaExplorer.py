import isatools.isatab as isatab
import os

__author__ = 'nsadawi'


def exploreISA(pathToISATABFile, verbose=True):
    """
        This function loops through the ISATAB file and lists its Studies and their associated Assays.
        :param pathToISATABFile: The path to the ISATAB file.
        :type xpathToISATABFile: str
        :param verbose: Whether (or not) to print out details of Studies and Assays (default: True)
        :raise FileNotFoundError: If pathToISATABFile does not contain file 'i_Investigation.txt'.
        """
    found = False
    try:
        # Load ISATAB file
        with open(os.path.join(pathToISATABFile,'i_Investigation.txt')) as fp:
            isa_tab_record = isatab.load(fp)
            found = True
        if verbose:
            print('In this ISATAB file you have:')
            for idx,st in enumerate(isa_tab_record.studies):
                print('Study: '+str(idx+1))
                print('\tStudy Identifier: '+st.identifier+', Study ID: '+st.id+', Study Filename: '+st.filename+', Study Title: '+st.title)
                print('\tThis Study has the following Assays:')
                for ix,a in enumerate(st.assays):
                    print('\tAssay: '+str(ix+1))
                    print('\t\tAssay Filename: '+a.filename+', Assay technology type: '+a.technology_type.term)
    except FileNotFoundError as err:
        raise err
    return found
