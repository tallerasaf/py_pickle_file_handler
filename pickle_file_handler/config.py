from numpy import ndarray
from pandas import DataFrame

from .pickle_methods.data_frame import (
    dump_data_frame_to_pickle_file,
    load_data_frame_from_pickle_file
)
from .pickle_methods.numpy_array import (
    dump_numpy_array_to_pickle_file,
    load_numpy_array_from_pickle_file
)

OBJECT_TYPE_PICKLE_LOAD_METHOD_MAPPING = {
    DataFrame: load_data_frame_from_pickle_file,
    ndarray: load_numpy_array_from_pickle_file,
}

OBJECT_TYPE_PICKLE_DUMP_METHOD_MAPPING = {
    DataFrame: dump_data_frame_to_pickle_file,
    ndarray: dump_numpy_array_to_pickle_file,
}
