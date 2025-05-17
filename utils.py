# utils.py
import os

def get_data_file(filename):
    """Returns the absolute path to a data file."""
    base_dir = os.path.dirname(os.path.abspath(_file_))
    return os.path.join(base_dir, 'data', filename)