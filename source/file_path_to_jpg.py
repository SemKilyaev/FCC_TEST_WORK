import os

def file_path():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1234.jpg')
    return file_path
