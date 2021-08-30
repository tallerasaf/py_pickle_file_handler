import numpy
from future.utils import PY3
from numpy import ndarray

from .consts import PICKLE_PY3_ENCODING
from .utils import (
    get_file_for_reading,
    get_file_for_writing
)


def load_numpy_array_from_pickle_file(file_path):
    # type: (str) -> ndarray
    with get_file_for_reading(file_path) as f:
        # noinspection PyTypeChecker
        pickled_arr = numpy.load(f, allow_pickle=True, encoding=PICKLE_PY3_ENCODING) \
            if PY3 else numpy.load(f, allow_pickle=True)
    return pickled_arr


def dump_numpy_array_to_pickle_file(file_path, numpy_array):
    # type: (str, ndarray) -> None
    with get_file_for_writing(file_path) as f:
        # noinspection PyTypeChecker
        numpy.save(arr=numpy_array, file=f)
