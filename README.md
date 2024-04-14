# Zuru

## Problem Overview
Python program that takes a JSON file (which contains the information of a directory in nested structure) and prints out its content in the console in the style of `ls` (Linux utility).

# Implement the command `ls`. The program should parse the JSON file and print the top-level directories and files.
```bash
abc
```

# Subtask 2: ls -A (2 points)
# Implement the argument `-A`, which prints all files and directories, including those starting with `.`.

# Subtask 3: ls -l (10 points)
# Implement the argument `-l`, which prints the results vertically with additional information like permissions, size, and time modified.

# Subtask 4: ls -l -r (3 points)
# Implement the argument `-r`, which prints the results in reverse order.

# Subtask 5: ls -l -r -t (5 points)
# Implement the argument `-t` that prints the results sorted by `time_modified` (oldest first).

# Subtask 6: ls -l -r -t --filter=<option> (5 points)
# Implement the argument `--filter=<option>`, where available options are `file` and `dir`.

# Subtask 7: Handle Paths (5 points)
# Handle navigating the structure within the JSON using paths.

# Subtask 8: ls -h (5 points)
# Show human-readable size.

# Subtask 9: ls --help (5 points)
# Implement `--help` option to print a helpful message.



# conda create -n env_name python=3.12.2 -y
# conda env list
# conda activate env_name
# conda remove -n env_name --all
# pip install -e . --user #can show change real time
# python setup.py install
# pip install .