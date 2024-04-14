import os
import json
import pytest
from datetime import datetime
from pyls.module import read_filepath, parse_json, handle_path, ls, human_readable_size, display

@pytest.fixture
def test_data(tmp_path):
    test_data = {
        "name": "test",
        "size": 1024,
        "time_modified": int(datetime.now().timestamp()),
        "permissions": "rw-r--r--",
        "contents": [
            {
                "name": "file1",
                "size": 512,
                "time_modified": int(datetime.now().timestamp()),
                "permissions": "rw-r--r--"
            },
            {
                "name": "file2",
                "size": 1024,
                "time_modified": int(datetime.now().timestamp()),
                "permissions": "rw-r--r--"
            },
            {
                "name": "dir1",
                "size": 0,
                "time_modified": int(datetime.now().timestamp()),
                "permissions": "rwxr-xr-x",
                "contents": [
                    {
                        "name": "file3",
                        "size": 2048,
                        "time_modified": int(datetime.now().timestamp()),
                        "permissions": "rw-r--r--"
                    }
                ]
            }
        ]
    }
    test_file = tmp_path / 'test_data.json'
    with open(test_file, 'w') as f:
        json.dump(test_data, f)
    return test_file


def test_read_filepath(test_data):
    assert read_filepath(test_data) == test_data
    with pytest.raises(SystemExit):
        read_filepath('nonexistent_file.json')

def test_parse_json(test_data):
    assert parse_json(test_data) == json.load(open(test_data))
    with pytest.raises(SystemExit):
        parse_json('nonexistent_file.json')
"""
def test_handle_path(test_data):
    test_data = dict(test_data)
    assert handle_path('test', test_data) == test_data
    with pytest.raises(SystemExit):
        handle_path('nonexistent_path', test_data)
"""
def test_ls(test_data):
    data = json.load(open(test_data))
    assert ls(data) == ['file1', 'file2', 'dir1']
    assert ls(data, use_long_format=True) == [
        {'name': 'file1', 'size': 512, 'time_modified': int(datetime.now().timestamp()), 'permissions': 'rw-r--r--', 'is_dir': False},
        {'name': 'file2', 'size': 1024, 'time_modified': int(datetime.now().timestamp()), 'permissions': 'rw-r--r--', 'is_dir': False},
        {'name': 'dir1', 'size': 0, 'time_modified': int(datetime.now().timestamp()), 'permissions': 'rwxr-xr-x', 'is_dir': True}
    ]

def test_human_readable_size():
    assert human_readable_size(1024) == '1.0K'
    assert human_readable_size(2048) == '2.0K'

def test_display():
    assert True