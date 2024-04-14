# Zuru

## Problem Overview
Python program that takes a JSON file (which contains the information of a directory in nested structure) and prints out its content in the console in the style of `ls` (Linux utility).

## The program should parse the JSON file and print the top-level directories and files.
```bash
python -m pyls
```
## Prints all files and directories, including those starting with `.`.
```bash
python -m pyls -A
```
## Prints the results vertically with additional information like permissions, size, and time modified.
```bash
python -m pyls -l
```
## Prints the results in reverse order.  -------
```bash
python -m pyls -l -r
```
## Prints the results sorted by `time_modified` (oldest first).
```bash
python -m pyls -l -r -t
```
## Filter with `file` and `dir`.
```bash
python -m pyls -l -r -t --filter=dir
```
```bash
python -m pyls -l -r -t --filter=file
```
## Handle navigating the structure within the JSON using paths.
```bash
python -m pyls -l parser
```
```bash
python -m pyls -l parser/parser.go
```
## Show human-readable size.
```bash
python -m pyls -h parser
```
## Option to print a helpful message.
```bash
python -m pyls --help
```
## To install this package as "pyls"
```bash
pip install -e . --user
```

# To Run This Project

## Create Virtual Environment
```bash
conda create -n env_name python=3.12.2 -y
```
## Activate Virtual Environment
```bash
conda activate env_name
```
## Install Dependency
```bash
pip install -rrequirements.txt
```
## Install Setup [Optional]
```bash
python setup.py install
```