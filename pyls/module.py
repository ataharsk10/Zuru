import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Union
FileInfo = Dict[str, Union[str, int, bool]]

# Function: Check filepath
def read_filepath(filepath:str) -> str:
    """
    This function will take the filepath,
    check the path existence and return filepath,
    else exit
    """
    try:
        if os.path.exists(filepath) == True:
            return filepath
        else:
            print(f"Error: '{filepath}' not found.")
            sys.exit(1)
    except Exception as e:
        print(f"Error: Occurred while checking filepath: {e}")
        sys.exit(1)


# Function:Parsing ".json" File
def parse_json(filepath:str) -> Dict:
    """
    This function will take the Directory Path as str, 
    and return the json file contains in the directory,
    else raise an error.
    """
    filepath = read_filepath(filepath)
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error: Occurred while parsing JSON: {e}")
        sys.exit(1)
    

# Check if the provided path is exists or not
def handle_path(path: str,data: Dict) -> Dict:
    """
    This function will take filepath and Data,
    traverse into the given filepath, return,
    if not found exit
    """
    try:
        path_components = path.split('/')
        current_directory = data
        #print(path_components)
        for component in path_components:
            if component == "." or component == "..":
                continue
            found = False
            for item in current_directory['contents']:
                if item['name'] == component:
                    current_directory = item
                    found = True
                    break
            if not found:
                print(f"error: cannot access '{path}': No such file or directory")
                return None
        #If current_directory is a file
        if ('contents' in current_directory) == False:
            prefix = './'
            traversed_dir = '/'.join(path_components)
            new_name = os.path.join(prefix, traversed_dir)
            current_directory['name'] = new_name
        
        return current_directory
    
    except Exception as e:
        print(f"Error: Occurred while handling path: {e}")
        sys.exit(1)


# Function to list out files and directories
def ls(directory: Dict, show_hidden: bool = False, use_long_format: bool = False) -> List[str]:
    """
    This function takes directory and list
    out the files
    """
    try:
        files=[]
        # If directory is a file
        if ('contents' in directory) == False:
            if use_long_format:
                files.append({
                    'name': directory['name'],
                    'size': directory['size'],
                    'time_modified': directory['time_modified'],
                    'permissions': directory['permissions'],
                    'is_dir': True if 'contents' in directory else False
                })
            else:
                files.append(file['name'])
        # If directory is dir
        else:
            for file in directory['contents']:
                if not show_hidden and file['name'].startswith('.'):
                    continue
                if use_long_format:
                    files.append({
                        'name': file['name'],
                        'size': file['size'],
                        'time_modified': file['time_modified'],
                        'permissions': file['permissions'],
                        'is_dir': True if 'contents' in file else False
                    })
                else:
                    files.append(file['name'])
        
        return files
    except Exception as e:
        print(f"Error: Occurred while listing directory: {e}")
        sys.exit(1)
    
#Human readable size function
def human_readable_size(size: int) -> str:
    """
    This function converts the size in to human readable format
    """
    try:
        suffixes = ['B', 'K', 'M', 'G', 'T']
        index = 0
        while size >= 1024 and index < len(suffixes) - 1:
            size /= 1024
            index += 1
        return f"{size:.1f}{suffixes[index]}"
    except Exception as e:
        print(f"Error: Occurred while converting size: {e}")
        sys.exit(1)

# Function to display 
def display(files: List[FileInfo], use_long_format: bool = False, reverse_order: bool = False, sort_by_time: bool = False, filter_option: Union[bool, str] = False, human_readable: bool = False) -> None:
    """
    This function takes files, and prints it
    """
    try:
        if use_long_format == False:
            print(' '.join(files))
        else:
            if sort_by_time:
                files.sort(key=lambda x: x['time_modified'])
            if reverse_order:
                files.reverse()
            if filter_option:
                if filter_option == 'file':
                    files = [file_info for file_info in files if not file_info['is_dir']]
                elif filter_option == 'dir':
                    files = [file_info for file_info in files if file_info['is_dir']]
                else:
                    print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'")
                    return None

            for file_info in files:
                modified_time = datetime.fromtimestamp(file_info['time_modified']).strftime('%b %d %H:%M')
                if human_readable:
                    filesize = human_readable_size(file_info['size'])
                else:
                    filesize = file_info['size']
                print(f"{file_info['permissions']} {filesize} {modified_time} {file_info['name']}")
    except Exception as e:
        print(f"Error: Occurred while displaying files: {e}")
        sys.exit(1)

        