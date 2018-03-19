import isatools.isatab as isatab
import os

__author__ = 'nsadawi'


def exploreISA(pathToISATABFile, verbose=True):
    """
        This function loops through the ISATAB file and lists its Studies and their associated Assays.
        :param pathToISATABFile: The path to the ISATAB file.
        :type xpathToISATABFile: str
        :param verbose: Whether (or not) to print out details of Studies and Assays (default: True)
        :type verbose: boolean
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


def getISAAassay(assay_num, study_num, path_to_isa_file):
    """
    This function returns an Assay object given the assay and study numbers in an ISA file
    Typically, you should use the exploreISA function to check the contents
    of the ISA file and retrieve the assay and study numbers you are interested in!
    :param assay_num: The Assay number (notice it's not zero-based index).
    :type assay_num: int
    :param study_num: The Study number (notice it's not zero-based index).
    :type study_num: int
    :param path_to_isa_file: The path to the ISATAB file
    :type path_to_isa_file: str
    :raise FileNotFoundError: If pathToISATABFile does not contain file 'i_Investigation.txt'.
    """
    from isatools import isatab
    try:
        isa = isatab.load(path_to_isa_file)
        std = isa.studies[study_num - 1]
        return std.assays[assay_num - 1]
    except FileNotFoundError as err:
        raise err


def getISAStudy(study_num, path_to_isa_file):
    """
    This function returns a Study object given the study number in an ISA file
    Typically, you should use the exploreISA function to check the contents
    of the ISA file and retrieve the study number you are interested in!
    :param study_num: The Study number (notice it's not zero-based index).
    :type study_num: int
    :param path_to_isa_file: The path to the ISATAB file
    :type path_to_isa_file: str
    :raise FileNotFoundError: If pathToISATABFile does not contain file 'i_Investigation.txt'.
    """
    from isatools import isatab
    try:
        isa = isatab.load(path_to_isa_file)
        return isa.studies[study_num - 1]
    except FileNotFoundError as err:
        raise err

def appendStudytoISA(study, path_to_isa_file):
    """
    This function appends a Study object to an ISA file
    Typically, you should use the exploreISA function to check the contents
    of the ISA file!
    :param study: The Study object.
    :type study: ISA Study object
    :param path_to_isa_file: The path to the ISATAB file
    :type path_to_isa_file: string
    :raise FileNotFoundError: If pathToISATABFile does not contain file 'i_Investigation.txt'.
    """
    from isatools import isatab
    try:
        isa = isatab.load(path_to_isa_file)
        isa.studies.append(study)
        return True
    except FileNotFoundError as err:
        raise err
    return False


def appendAssayToStudy(assay, study_num, path_to_isa_file):
    """
    This function appends an Assay object to a study in an ISA file
    Typically, you should use the exploreISA function to check the contents
    of the ISA file and retrieve the assay and study number you are interested in!
    :param assay: The Assay
    :type assay_num: ISA Assay object
    :param study_num: The Study number (notice it's not zero-based index).
    :type study_num: int
    :param path_to_isa_file: The path to the ISATAB file
    :type path_to_isa_file: string
    :raise FileNotFoundError: If pathToISATABFile does not contain file 'i_Investigation.txt'.
    """
    from isatools import isatab
    try:
        isa = isatab.load(path_to_isa_file)
        std = isa.studies[study_num - 1]
        std.assays.append(assay)
        return True
    except FileNotFoundError as err:
        raise err
    return False

def dropAssayFromStudy(assay_num, study_num, path_to_isa_file):
    """
    This function removes an Assay from a study in an ISA file
    Typically, you should use the exploreISA function to check the contents
    of the ISA file and retrieve the assay and study numbers you are interested in!
    :param assay_num: The Assay number (notice it's 1-based index).
    :type assay_num: int
    :param study_num: The Study number (notice it's 1-based index).
    :type study_num: int
    :param path_to_isa_file: The path to the ISATAB file
    :type path_to_isa_file: string
    :raise FileNotFoundError: If pathToISATABFile does not contain file 'i_Investigation.txt'.
    """
    from isatools import isatab
    try:
        isa = isatab.load(path_to_isa_file)
        std = isa.studies[study_num - 1]
        assays = std.assays
        del assays[assay_num - 1]
        return True
    except FileNotFoundError as err:
        raise err
    return False

def dropStudyFromISA(study_num, path_to_isa_file):
    """
    This function removes a study from an ISA file
    Typically, you should use the exploreISA function to check the contents
    of the ISA file and retrieve the study number you are interested in!
    :param study_num: The Study number (notice it's 1-based index).
    :type study_num: int
    :param path_to_isa_file: The path to the ISATAB file
    :type path_to_isa_file: string
    :raise FileNotFoundError: If pathToISATABFile does not contain file 'i_Investigation.txt'.
    """
    from isatools import isatab
    try:
        isa = isatab.load(path_to_isa_file)
        studies = isa.studies
        del studies[study_num - 1]
        return True
    except FileNotFoundError as err:
        raise err
    return False
