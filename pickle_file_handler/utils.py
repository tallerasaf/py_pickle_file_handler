from builtins import str
from pathlib import Path, PosixPath
from typing import List, Union

from future.utils import string_types

PICKLE_FILE_EXT = '.p'
NUM_PY_FILE_EXT = '.npy'
ALLOWED_FILE_EXTENSIONS = (PICKLE_FILE_EXT, NUM_PY_FILE_EXT, '.pkl', '.pickle', '.dat')


def get_current_folder_pickle_file_path(__file__, file_name):
    # type: (str, str) -> str
    return get_pickle_file_path(get_parent_path(__file__), file_name)


def get_current_folder_path(__file__, folder_names):
    # type: (str, Union[str, List[str]]) -> Union[str, PosixPath]
    return get_combine_folder_path(get_parent_path(__file__), folder_names)


def get_combine_folder_path(base_dir, folder_names):
    # type: (Union[str, PosixPath], Union[str, List[str]]) -> Union[Path, PosixPath]
    if folder_names is None:
        return base_dir
    return Path(base_dir).joinpath(get_folder_path(folder_names))


def get_folder_path(folder_names):
    # type: (Union[str, List[str]]) -> Union[str, PosixPath]
    if isinstance(folder_names, string_types):
        return folder_names
    if isinstance(folder_names, list):
        return Path.joinpath(*map(Path, folder_names))
    raise TypeError('Unable to get_folder_path, folder_names must be list or str.')


def get_parent_path(file_path):
    # type: (str) -> Union[Path, PosixPath]
    return Path(file_path).parent


def get_pickle_file_path(folder_path, file_name):
    # type: (Union[str, PosixPath], str) -> str
    return join_path(folder_path, add_pickle_ext(file_name))


def join_path(folder_path, file_name):
    # type: (Union[str, PosixPath], str) -> str
    # noinspection PyTypeChecker
    return str(Path(folder_path).joinpath(file_name))


def add_pickle_ext(file_name):
    # type: (str) -> str
    if file_name.endswith(ALLOWED_FILE_EXTENSIONS):
        return file_name
    assert '.' not in file_name, 'Invalid file name "{}" for pickle.'.format(file_name)
    return '{}{}'.format(file_name, PICKLE_FILE_EXT)
