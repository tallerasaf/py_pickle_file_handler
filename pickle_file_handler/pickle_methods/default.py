from typing import Any, IO

from future.moves import pickle
from future.utils import PY3

from .consts import PICKLE_PY2_PROTOCOL, PICKLE_PY3_ENCODING
from .utils import (
    get_file_for_reading,
    get_file_for_writing
)


def load_object_from_pickle_file(file_path):
    # type: (str) -> object
    with get_file_for_reading(file_path) as f:
        pickled_obj = load_object_from_pickle_file_stream(f)
    return pickled_obj


def load_object_from_pickle_file_stream(file_stream):
    # type: (IO[Any]) -> object
    return pickle.load(file_stream, encoding=PICKLE_PY3_ENCODING) if PY3 else pickle.load(file_stream)


def dump_object_to_pickle_file(file_path, my_object):
    # type: (str, object) -> None
    with get_file_for_writing(file_path) as f:
        dump_object_to_pickle_file_stream(f, my_object)


def dump_object_to_pickle_file_stream(file_stream, my_object):
    # type: (IO[Any], object) -> None
    pickle.dump(obj=my_object, file=file_stream, protocol=PICKLE_PY2_PROTOCOL)


def load_pickle_from_string(my_str):
    # type: (str) -> str
    """
    Py2 - Read a pickled object hierarchy from a string.
          Characters in the string past the pickled object's representation are ignored.
    Py3 - Return the reconstituted object hierarchy of the pickled representation data of an object.
          data must be a bytes-like object.
    """
    # noinspection PyTypeChecker
    return pickle.loads(my_str, encoding=PICKLE_PY3_ENCODING) if PY3 else pickle.loads(my_str)


def dump_object_to_string(my_object):
    # type: (object) -> str
    """
    Py2 - Return the pickled representation of the object as a string, instead of writing it to a file.
    Py3 - Return the pickled representation of the object obj as a bytes object,
          instead of writing it to a file.
    """
    # noinspection PyTypeChecker
    return pickle.dumps(obj=my_object, protocol=PICKLE_PY2_PROTOCOL)
