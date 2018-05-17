import os
from pathlib import Path
import pickle

def store_movies_by_name(root_path):
    files_by_name = {}
    for path, dirs, files in os.walk(root_path):
        for file in files:
            files_by_name[file]={"path":root_path}
    home = str(Path.home())
    with open(home+"/.downl-od.pickle", 'wb') as f:
        pickle.dump(files_by_name, f)
    return files_by_name

def load_movies_by_name():
    home = str(Path.home())
    with open(home+"/.downl-od.pickle", 'rb') as f:
        files_by_name = pickle.load(f)
    return files_by_name
