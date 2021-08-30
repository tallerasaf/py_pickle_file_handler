"""
- Python file modes -
Don’t confuse, read about every mode below:
-
'r' -   for reading – The file pointer is placed at the beginning of the file. This is the default mode.
'r+' -  Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
'w' -   Opens a file for writing only. Overwrites the file if the file exists.
        If the file does not exist, creates a new file for writing.
'w+' -  Opens a file for both writing and reading. Overwrites the existing file if the file exists.
        If the file does not exist, it creates a new file for reading and writing.
'rb' -  Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
'rb+' - Opens a file for both reading and writing in binary format.
'wb+' - Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists.
        If the file does not exist, it creates a new file for reading and writing.
'a' -   Opens a file for appending. The file pointer is at the end of the file if the file exists.
        That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
'ab' -  Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists.
        That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
'a+' -  Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists.
        The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'ab+' - Opens a file for both appending and reading in binary format.
        The file pointer is at the end of the file if the file exists.
        The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'x' -   open for exclusive creation, failing if the file already exists (Python 3)
"""

import io
from io import BytesIO
from typing import Any, IO, Union

from future.utils import PY3, string_types
from six import StringIO

from .consts import DEFAULT_ENCODING

BINARY_READING_MODE = 'rb'
BINARY_WRITING_MODE = 'wb'
BINARY_READING_AND_WRITING_MODE = 'wb+'
READING_AND_WRITING_MODE = 'w+'


def get_file_for_reading(file_path):
    # type: (str) -> IO[Any]
    return _get_file(file_path, BINARY_READING_MODE)


def get_file_for_writing(file_path):
    # type: (str) -> IO[Any]
    return _get_file(file_path, BINARY_WRITING_MODE)


def _get_file(file_path, mode):
    # type: (str, str) -> IO[Any]
    return io.open(file_path, mode)


def get_mode_for_both_writing_and_reading(file_stream):
    # type: (Union[StringIO, BytesIO]) -> str
    if isinstance(file_stream, StringIO):
        return READING_AND_WRITING_MODE
    return BINARY_READING_AND_WRITING_MODE


def get_stream_io(data):
    # type: (Union[str, bytes]) -> Union[StringIO, BytesIO]
    if PY3 and isinstance(data, string_types):
        data = data.encode(DEFAULT_ENCODING)
        return BytesIO(data)
    elif isinstance(data, string_types):
        return StringIO(data)
    return BytesIO(data)
