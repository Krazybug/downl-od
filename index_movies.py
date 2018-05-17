import os
from pathlib import Path
import pickle

movie_file_ext = [   '.3g2','.3gp','.3gp2','.3gpp','.60d','.ajp','.asf',
                     '.asx','.avchd','.avi','.bik','.bix','.box','.cam',
                     '.dat','.divx','.dmf','.dv','.dvr-ms','.evo','flc',
                     '.fli','.flic','.flv','.flx','.gvi','.gvp','.h264',
                     '.m1v','.m2p','.m2ts','.m2v','.m4e','.m4v','.mjp',
                     '.mjpeg','.mjpg','.mkv','.moov','.mov','.movhd',
                     '.movie','.movx','.mp4','.mpe','.mpeg','.mpg','.mpv',
                     '.mpv2','.mxf','.nsv','.nut','.ogg','.ogm','.omf',
                     '.ps','.qt','.ram','.rm','.rmvb','.swf','.ts','.vfw',
                     '.vid','.video','.viv','.vivo','.vob','.vro','.wm',
                     '.wmv','.wmx','.wrap','.wvx','.wx','.x264','.xvid']

subtitle_file_ext = ['.srt', '.sub', '.sbv']


movies_by_name_path=str(Path.home())+"/.downl-od/"
movies_by_name_file= "movies_by_name.pickle"


def store_movies_by_name(root_path, movies_by_name_path=movies_by_name_path):
    m_path=movies_by_name_path+movies_by_name_file
    if os.path.exists(m_path):
        files_by_name = load_movies_by_name(movies_by_name_path)
    else:
        files_by_name = {}
    for path, dirs, files in os.walk(root_path):
        for file in files:
            if os.path.splitext(file)[-1] in movie_file_ext+subtitle_file_ext:
                files_by_name[file]={"path":root_path}
    os.makedirs(movies_by_name_path, exist_ok=True)
    with open(m_path, 'wb') as f:
        pickle.dump(files_by_name, f)
    return files_by_name

def load_movies_by_name(movies_by_name_path=movies_by_name_path):
    with open(movies_by_name_path+movies_by_name_file, 'rb') as f:
        files_by_name = pickle.load(f)
    return files_by_name
