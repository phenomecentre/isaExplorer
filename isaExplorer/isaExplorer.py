import isatools.isatab as isatab
import os

__author__ = 'nsadawi'


def exploreISA(pathToISATABFile, verbose=True):
    found = False
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

    return found
