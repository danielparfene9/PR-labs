import os
import shutil

def clean_directory(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)