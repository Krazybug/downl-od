import pytest
import os
import shutil
import tempfile
from ..index_movies import store_movies_by_name, load_movies_by_name



root_dir=tempfile.mkdtemp()

@pytest.fixture
def create_fake_tree():
    i=0
    with open("files.txt") as f:
        for l in f.readlines():
            dir=root_dir+i*"/a"+"/"
            os.makedirs(dir, exist_ok=True)
            filename=l.strip()
            print(filename)
            with open(dir+filename, 'w'):
                pass
            if i<5:
                i+=1
            else:
                i=0
    yield
    shutil.rmtree(root_dir)

def test_store_movies_by_name(create_fake_tree):
    files_by_name = store_movies_by_name(root_dir)
    print(files_by_name)
    assert len(files_by_name) != 0
    files_by_name_out = load_movies_by_name()
    assert files_by_name == files_by_name_out
