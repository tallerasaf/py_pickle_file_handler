import os
from builtins import range
from unittest import TestCase
from unittest.mock import patch

import numpy
import pandas
from numpy import ndarray
from pandas import DataFrame

import pickle_file_handler
from pickle_file_handler.utils import get_current_folder_pickle_file_path, get_pickle_file_path


class PickleFileHandlerUnitTests(TestCase):
    maxDiff = None
    TEST_FILE_NAME = 'test_pickle_111'

    def setUp(self):
        self.should_mock_local_disk_access = False
        super(PickleFileHandlerUnitTests, self).setUp()
        self.file_path = get_current_folder_pickle_file_path(__file__, self.TEST_FILE_NAME)
        self.dict_to_pickle = {chr(value): index for index, value in enumerate(range(97, 123))}
        self.data_frame_to_pickle = DataFrame(numpy.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        self.numpy_array_to_pickle = numpy.random.rand(40, 22, 20, 50, 30)

    def test_dict(self):
        pickle_file_handler.dump_to_pickle_file_in_current_folder(__file__,
                                                                  file_name=self.TEST_FILE_NAME,
                                                                  my_object=self.dict_to_pickle)

        result = pickle_file_handler.load_from_pickle_file_in_current_folder(__file__, file_name=self.TEST_FILE_NAME)
        # noinspection PyTypeChecker
        self.assertDictEqual(result, self.dict_to_pickle)
        os.remove(self.file_path)

    @patch('pickle_file_handler.pickle_file_by_type.load_object_from_pickle_file')
    @patch('pickle_file_handler.pickle_file_by_type.dump_object_to_pickle_file')
    def test_mocked_dict(self, mocked_dump_object_to_pickle_file, mocked_load_object_from_pickle_file):
        pickle_file_handler.dump_to_pickle_file_in_current_folder(__file__,
                                                                  file_name=self.TEST_FILE_NAME,
                                                                  my_object=self.dict_to_pickle)
        mocked_dump_object_to_pickle_file.assert_called_once_with(self.file_path, self.dict_to_pickle)
        pickle_file_handler.load_from_pickle_file_in_current_folder(__file__, file_name=self.TEST_FILE_NAME)
        mocked_load_object_from_pickle_file.assert_called_once_with(self.file_path)

    def test_data_frame(self):
        pickle_file_handler.dump_to_pickle_file_in_current_folder(__file__,
                                                                  file_name=self.TEST_FILE_NAME,
                                                                  my_object=self.data_frame_to_pickle)
        result = pickle_file_handler.load_data_frame_from_pickle_file_in_current_folder(__file__,
                                                                                        file_name=self.TEST_FILE_NAME)
        # noinspection PyTypeChecker
        pandas.testing.assert_frame_equal(result, self.data_frame_to_pickle)
        os.remove(self.file_path)

    @patch('pickle_file_handler.pickle_file_by_type.OBJECT_TYPE_PICKLE_LOAD_METHOD_MAPPING')
    @patch('pickle_file_handler.pickle_file_by_type.OBJECT_TYPE_PICKLE_DUMP_METHOD_MAPPING')
    def test_mocked_data_frame(self, mocked_object_type_pickle_dump_method_mapping,
                               mocked_object_type_pickle_load_method_mapping):
        pickle_file_handler.dump_to_pickle_file_in_current_folder(__file__,
                                                                  file_name=self.TEST_FILE_NAME,
                                                                  my_object=self.data_frame_to_pickle)
        mocked_object_type_pickle_dump_method_mapping[DataFrame].assert_called_once_with(self.file_path,
                                                                                         self.data_frame_to_pickle)
        pickle_file_handler.load_data_frame_from_pickle_file_in_current_folder(__file__, file_name=self.TEST_FILE_NAME)
        mocked_object_type_pickle_load_method_mapping[DataFrame].assert_called_once_with(self.file_path)

    def test_numpy_array(self):
        pickle_file_handler.dump_to_pickle_file_in_current_folder(__file__,
                                                                  file_name=self.TEST_FILE_NAME,
                                                                  my_object=self.numpy_array_to_pickle)
        result = pickle_file_handler.load_numpy_array_from_pickle_file_in_current_folder(__file__,
                                                                                         file_name=self.TEST_FILE_NAME)
        # noinspection PyTypeChecker
        numpy.testing.assert_array_almost_equal(result, self.numpy_array_to_pickle)
        os.remove(self.file_path)

    @patch('pickle_file_handler.pickle_file_by_type.OBJECT_TYPE_PICKLE_LOAD_METHOD_MAPPING')
    @patch('pickle_file_handler.pickle_file_by_type.OBJECT_TYPE_PICKLE_DUMP_METHOD_MAPPING')
    def test_mocked_numpy_array(self, mocked_object_type_pickle_dump_method_mapping,
                                mocked_object_type_pickle_load_method_mapping):
        pickle_file_handler.dump_to_pickle_file_in_current_folder(__file__,
                                                                  file_name=self.TEST_FILE_NAME,
                                                                  my_object=self.numpy_array_to_pickle)
        mocked_object_type_pickle_dump_method_mapping[ndarray].assert_called_once_with(self.file_path,
                                                                                       self.numpy_array_to_pickle)
        pickle_file_handler.load_numpy_array_from_pickle_file_in_current_folder(__file__, file_name=self.TEST_FILE_NAME)
        mocked_object_type_pickle_load_method_mapping[ndarray].assert_called_once_with(self.file_path)

    def test_get_pickle_file_path(self):
        self.assertEqual(get_pickle_file_path(folder_path='/aaa/bbb/cccc', file_name='blabla'),
                         '/aaa/bbb/cccc/blabla.p')
        self.assertEqual(get_pickle_file_path(folder_path='/aaa/bbb/cccc', file_name='blabla.p'),
                         '/aaa/bbb/cccc/blabla.p')
        self.assertEqual(get_pickle_file_path(folder_path='/aaa/bbb/cccc', file_name='blabla.npy'),
                         '/aaa/bbb/cccc/blabla.npy')
        with self.assertRaises(AssertionError):
            get_pickle_file_path(folder_path='/aaa/bbb/cccc', file_name='blabla.xor')
