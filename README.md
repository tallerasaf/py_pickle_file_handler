# **_pickle_file_handler_**! 🔥

## **Pickle File Handler for Python(Compatible with Py2 and Py3).**

- Replace the usage of:
    - **_pickle_**(_load_, _dump_)(_object_).
    - **_numpy_**(_load_, _save_)(_ndarray_).
    - **_pandas_**(_read_pickle_, _to_pickle_)(_DataFrame_).
- The new lib will fully support both **Python 2.7** and **Python 3.7**!
- Will help you to write simpler, more readable code with fewer lines and avoid duplicate code.

### Functions:

- **_For Any Object Type_**:
    - **_dump_**:
        - dump_to_pickle_file_in_base_dir
        - dump_to_pickle_file_in_folders
        - dump_to_pickle_file_in_current_folder
        - dump_to_pickle_file_in_folder
        - dump_to_pickle_file
    - **_load:_**
        - load_from_pickle_file_in_current_folder
        - load_from_pickle_file_in_base_dir
        - load_from_pickle_file_in_folders
        - oad_from_pickle_file_in_folder
        - load_from_pickle_file
- **_pandas.DataFrame Only_**:
    - load_data_frame_from_pickle_file_in_current_folder
    - load_data_frame_from_pickle_file_in_base_dir
    - load_data_frame_from_pickle_file_in_folders
    - load_data_frame_from_pickle_file_in_folder
    - load_data_frame_from_pickle_file
- **_numpy.ndarray Only_**:
    - load_numpy_array_from_pickle_file_in_current_folder
    - load_numpy_array_from_pickle_file_in_base_dir
    - load_numpy_array_from_pickle_file_in_folders
    - load_numpy_array_from_pickle_file_in_folder
    - load_numpy_array_from_pickle_file

### Example Usage:

```
    import pickle_file_handler

    df1 = pickle_file_handler.load_data_frame_from_pickle_file_in_folder(
        folder_path='folder_1/folder_2/folder_3',
        file_name='some_file_name_1'
    )

    df1 = pickle_file_handler.load_data_frame_from_pickle_file_in_current_folder(__file__,
                                                                                 file_name='some_file_name_1')

    # Load from inner folder inside the current folder:
    from functools import partial

    load_data_frame_from_pickle_file = partial(
        pickle_file_handler.load_from_pickle_file_in_current_folder,
        __file__,
        folder_names=['some_folder_name_1', 'some_folder_name_2']
    )
    df1 = load_data_frame_from_pickle_file(file_name='some_file_name_1')
    df2 = load_data_frame_from_pickle_file(file_name='some_file_name_1')
```

###### ![Pickle Rick](https://i.pinimg.com/originals/2e/91/2d/2e912d825e7f76887c33631d89abe900.jpg)

## Author:
- [Asaf Taller](https://github.com/tallerasaf)
##### Copyright (C) [2021] [tallerasaf].
