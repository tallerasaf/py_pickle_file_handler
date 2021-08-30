from pathlib import Path, PosixPath
from typing import List, Optional, Union

from numpy import ndarray
from pandas import DataFrame

from .pickle_file_by_type import (
    dump_to_pickle_file,
    load_from_pickle_file
)
from .utils import (
    get_combine_folder_path, get_current_folder_path, get_pickle_file_path
)


# region data_frame
def load_data_frame_from_pickle_file_in_current_folder(__file__, file_name, folder_names=None):
    # type: (str, str, Optional[Union[str, List[str]]]) -> DataFrame
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_current_folder(__file__, file_name, folder_names, expected_type=DataFrame)


def load_data_frame_from_pickle_file_in_base_dir(base_dir, file_name, folder_names=None):
    # type: (str, str, Optional[Union[str, List[str]]]) -> DataFrame
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_base_dir(base_dir, file_name, folder_names, expected_type=DataFrame)


def load_data_frame_from_pickle_file_in_folders(folders_path, file_name):
    # type: (List[Union[str, PosixPath]], str) -> DataFrame
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_folders(folders_path, file_name, expected_type=DataFrame)


def load_data_frame_from_pickle_file_in_folder(folder_path, file_name):
    # type: (str, str) -> DataFrame
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_folder(folder_path, file_name, expected_type=DataFrame)


def load_data_frame_from_pickle_file(file_path):
    # type: (str) -> DataFrame
    # noinspection PyTypeChecker
    return load_from_pickle_file(file_path=file_path, expected_type=DataFrame)


# endregion

# region numpy_array
def load_numpy_array_from_pickle_file_in_current_folder(__file__, file_name, folder_names=None):
    # type: (str, str, Optional[Union[str, List[str]]]) -> ndarray
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_current_folder(__file__, file_name, folder_names, expected_type=ndarray)


def load_numpy_array_from_pickle_file_in_base_dir(base_dir, file_name, folder_names=None):
    # type: (str, str, Optional[Union[str, List[str]]]) -> ndarray
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_base_dir(base_dir, file_name, folder_names, expected_type=ndarray)


def load_numpy_array_from_pickle_file_in_folders(folders_path, file_name):
    # type: (List[Union[str, PosixPath]], str) -> ndarray
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_folders(folders_path, file_name, expected_type=ndarray)


def load_numpy_array_from_pickle_file_in_folder(folder_path, file_name):
    # type: (str, str) -> ndarray
    # noinspection PyTypeChecker
    return load_from_pickle_file_in_folder(folder_path, file_name, expected_type=ndarray)


def load_numpy_array_from_pickle_file(file_path):
    # type: (str) -> ndarray
    # noinspection PyTypeChecker
    return load_from_pickle_file(file_path=file_path,
                                 expected_type=ndarray)


# endregion


# region default
# region default - load
def load_from_pickle_file_in_current_folder(__file__, file_name, folder_names=None, expected_type=None):
    # type: (str, str, Optional[Union[str, List[str]]], Optional[type]) -> object
    return load_from_pickle_file_in_folder(folder_path=get_current_folder_path(__file__, folder_names),
                                           file_name=file_name,
                                           expected_type=expected_type)


def load_from_pickle_file_in_base_dir(base_dir, file_name, folder_names=None, expected_type=None):
    # type: (str, str, Optional[Union[str, List[str]]], Optional[type]) -> object
    return load_from_pickle_file_in_folder(folder_path=get_combine_folder_path(base_dir, folder_names),
                                           file_name=file_name,
                                           expected_type=expected_type)


def load_from_pickle_file_in_folders(folders_path, file_name, expected_type=None):
    # type: (List[Union[str, PosixPath]], str, Optional[type]) -> object
    return load_from_pickle_file_in_folder(folder_path=Path.joinpath(*folders_path),
                                           file_name=file_name,
                                           expected_type=expected_type)


def load_from_pickle_file_in_folder(folder_path, file_name, expected_type=None):
    # type: (Union[str, PosixPath], str, Optional[type]) -> object
    return load_from_pickle_file(file_path=get_pickle_file_path(folder_path, file_name),
                                 expected_type=expected_type)


# endregion
# region default - dump
def dump_to_pickle_file_in_base_dir(base_dir, file_name, my_object, folder_names=None):
    # type: (str, str, object, Optional[Union[str, List[str]]]) -> object
    return dump_to_pickle_file_in_folder(folder_path=get_combine_folder_path(base_dir, folder_names),
                                         file_name=file_name,
                                         my_object=my_object)


def dump_to_pickle_file_in_folders(folders_path, file_name, my_object):
    # type: (List[Union[str, PosixPath]], str, object) -> object
    return dump_to_pickle_file_in_folder(folder_path=Path.joinpath(*folders_path),
                                         file_name=file_name,
                                         my_object=my_object)


def dump_to_pickle_file_in_current_folder(__file__, file_name, my_object, folder_names=None):
    # type: (str, str, object, Optional[Union[str, List[str]]]) -> None
    dump_to_pickle_file_in_folder(folder_path=get_current_folder_path(__file__, folder_names),
                                  file_name=file_name,
                                  my_object=my_object)


def dump_to_pickle_file_in_folder(folder_path, file_name, my_object):
    # type: (Union[str, PosixPath], str, object) -> None
    dump_to_pickle_file(file_path=get_pickle_file_path(folder_path, file_name),
                        my_object=my_object)
# endregion
# endregion
