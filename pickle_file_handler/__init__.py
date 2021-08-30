__doc__ = 'PickleFileHandler Lib! -> A new Pickle File Handler! (Compatible with Py2 and Py3).'
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
