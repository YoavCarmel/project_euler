import pickle


def pickle_to_file(obj, filename):
    """
    :param obj: object to write to file
    :param filename: the file to write to
    """
    with open(filename, 'wb') as outfile:
        pickle.dump(obj, outfile)


def pickle_from_file(filename):
    """
    :param filename: file to read from
    :return: the object in file
    """
    with open(filename, 'rb') as infile:
        return pickle.load(infile)
