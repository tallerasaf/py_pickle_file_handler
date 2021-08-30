"""
PickleFileHandler Lib! -> A new Pickle File Handler! (Compatible with Py2 and Py3).
# Python 2-3 compatible code.

# https://python-future.org/compatible_idioms.html
- From now on if you wanna use pickle you should use it via PickleFileHandler.
- Replace the usage of: pickle(load,dump)(object),numpy(load,save)(ndarray),pandas(read_pickle,to_pickle)(DataFrame).
- The new lib will fully support both Python 2.7 and Python 3.7!
- Will help you to write simpler, more readable code with fewer lines and avoid duplicate code.
# Usage:
--
    import pickle_file_handler
    data = pickle_file_handler.load_data_frame_from_pickle_file_in_folder(
        folder_path=self._data_base_path,
        file_name='predicted_data'
    )
--
    from functools import partial

    my_object = pickle_file_handler.load_data_frame_from_pickle_file_in_current_folder(__file__, file_name='bla')

    load_data_frame_from_pickle_file = partial(
        pickle_file_handler.load_data_frame_from_pickle_file_in_inner_folder, __file__,
        folder_names=['Data', 'PriceTag_data']
    )
    load_data_frame_from_pickle_file(file_name='before_data')
--

Methods:
For Any Object Type:
  dump
    1. dump_to_pickle_file_in_base_dir
    2. dump_to_pickle_file_in_folders
    3. dump_to_pickle_file_in_current_folder
    4. dump_to_pickle_file_in_folder
    5. dump_to_pickle_file
  load
    1. load_from_pickle_file_in_current_folder
    2. load_from_pickle_file_in_base_dir
    3. load_from_pickle_file_in_folders
    4. load_from_pickle_file_in_folder
    5. load_from_pickle_file
pandas.DataFrame Only:
    1. load_data_frame_from_pickle_file_in_current_folder
    2. load_data_frame_from_pickle_file_in_base_dir
    3. load_data_frame_from_pickle_file_in_folders
    4. load_data_frame_from_pickle_file_in_folder
    5. load_data_frame_from_pickle_file
numpy.ndarray Only:
    1. load_numpy_array_from_pickle_file_in_current_folder
    2. load_numpy_array_from_pickle_file_in_base_dir
    3. load_numpy_array_from_pickle_file_in_folders
    4. load_numpy_array_from_pickle_file_in_folder
    5. load_numpy_array_from_pickle_file
"""

__author__ = 'tallerasaf'
__all__ = []

from .pickle_file_by_type import (
    dump_to_pickle_file,
    load_from_pickle_file
)
from .pickle_handler import *
from .pickle_methods.default import (
    dump_object_to_pickle_file_stream,
    dump_object_to_string,
    load_object_from_pickle_file_stream,
    load_pickle_from_string
)
from .utils import (
    get_pickle_file_path
)
