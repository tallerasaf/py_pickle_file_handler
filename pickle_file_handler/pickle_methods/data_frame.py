import pandas
from pandas import DataFrame

from .consts import PICKLE_PY2_PROTOCOL


def load_data_frame_from_pickle_file(file_path):
    # type: (str) -> DataFrame
    return pandas.read_pickle(file_path)


def dump_data_frame_to_pickle_file(file_path, data_frame):
    # type: (str, DataFrame) -> None
    data_frame.to_pickle(path=file_path, protocol=PICKLE_PY2_PROTOCOL)
