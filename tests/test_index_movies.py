import pytest
import os
import shutil
import tempfile

import sys
sys.path.append('.')
from index_movies import movie_file_ext, subtitle_file_ext, store_movies_by_name, load_movies_by_name


root_dir=tempfile.mkdtemp()
@pytest.fixture
def create_fake_tree():
    i=0
    with open("./tests/files.txt") as f:
        for l in f.readlines():
            dir=root_dir+i*"/a"+"/"
            os.makedirs(dir, exist_ok=True)
            filename=l.strip()
            with open(dir+filename, 'w'):
                pass
            if i<5:
                i+=1
            else:
                i=0
    yield
    shutil.rmtree(root_dir)

def test_store_movies_by_name_should_filter_movies_and_subtitles_by_ext(create_fake_tree):
    home_dir=tempfile.mkdtemp()
    files_by_name = store_movies_by_name(root_dir, home_dir)
    shutil.rmtree(home_dir)
    assert len(files_by_name) != 0
    for file in files_by_name.keys():
        assert  os.path.splitext(file)[-1] in movie_file_ext+subtitle_file_ext

def test_store_movies_by_name_should_persist_files(create_fake_tree):
    home_dir=tempfile.mkdtemp()
    files_by_name = store_movies_by_name(root_dir, home_dir)
    files_by_name_out = load_movies_by_name(home_dir)
    shutil.rmtree(home_dir)
    assert len(files_by_name) != 0
    assert files_by_name == files_by_name_out

def test_store_movies_by_name_should_store_new_files():
    home_dir=tempfile.mkdtemp()
    dir=tempfile.mkdtemp()
    os.makedirs(dir, exist_ok=True)
    with open(dir+"/a.avi", 'w'):
                pass
    files_by_name = store_movies_by_name(dir, home_dir)
    shutil.rmtree(dir)
    dir=tempfile.mkdtemp()
    with open(dir+"/b.avi", 'w'):
                pass
    files_by_name = store_movies_by_name(dir, home_dir)
    shutil.rmtree(dir)
    shutil.rmtree(home_dir)
    assert "a.avi" in files_by_name

# def test_store_movies_by_name_should_purge_deleted_files():
#     home_dir=tempfile.mkdtemp()
#     dir=tempfile.mkdtemp()
#     os.makedirs(dir, exist_ok=True)
#     with open(dir+"/a.avi", 'w'):
#                 pass
#     files_by_name = store_movies_by_name(dir, home_dir)
#     os.remove(dir+"/a.avi")
#     files_by_name = store_movies_by_name(dir, home_dir)
#     shutil.rmtree(dir)
#     shutil.rmtree(home_dir)
#     assert files_by_name == {}
