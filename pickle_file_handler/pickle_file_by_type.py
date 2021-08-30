from typing import Optional

from .config import (
    OBJECT_TYPE_PICKLE_DUMP_METHOD_MAPPING,
    OBJECT_TYPE_PICKLE_LOAD_METHOD_MAPPING
)
from .pickle_methods.default import (
    dump_object_to_pickle_file,
    load_object_from_pickle_file
)


def load_from_pickle_file(file_path, expected_type=None):
    # type: (str, Optional[type]) -> object
    try:
        return OBJECT_TYPE_PICKLE_LOAD_METHOD_MAPPING[expected_type](file_path)
    except KeyError:
        return load_object_from_pickle_file(file_path)


def dump_to_pickle_file(file_path, my_object):
    # type: (str, object) -> None
    try:
        OBJECT_TYPE_PICKLE_DUMP_METHOD_MAPPING[type(my_object)](file_path, my_object)
    except KeyError:
        dump_object_to_pickle_file(file_path, my_object)
