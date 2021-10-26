"""
Program which converts vob files to mkv
"""

# Imports
import os
from makemkv import MakeMKV
from makemkv import ProgressParser

# install git live plugin for pycharm
# https://pypi.org/project/makemkv/
# https://www.internalpointers.com/post/convert-vob-files-mkv-ffmpeg


def draw_file_tree(path: str, depth: int) -> None:
    """
    recursive function which draws file tree of a given folder

    :param path: str
        path of a current folder
    :param depth: int
        how deep from mother folder the program currently is
    :return:
    """
    try:
        for f in os.listdir(r"" + path):
            name, ext = os.path.splitext(f)
            if os.path.isfile(f):
                print("  " * depth + "-" + f)
                if is_movie_to_convert():
                    convert_movie(path, name, ext)
            elif os.path.isdir(f):
                print("  " * depth + "-" + name)
                draw_file_tree(path + f"/{name}", depth + 1)
            else:
                print("  " * depth + "-" + name + " !(Is not file nor folder)")
    except FileNotFoundError:
        # if the files starts with . - the program thinks it is a folder. This try except-block resolves it
        print("  " * depth + "-" + path.split("/")[-1])


def is_movie_to_convert(path: str, name: str, extension: str) -> bool:
    pass


def convert_movie(path: str) -> None:
    with ProgressParser() as progress:
        makemkv = MakeMKV(0, progress_handler=progress.parse_progress)
        makemkv.mkv(0, path)

draw_file_tree(os.getcwd(), 0)