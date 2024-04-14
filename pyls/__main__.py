from pyls.module import parse_json,handle_path,ls,display
import argparse

# Function Expand Arguments
def expand() -> None:
    """
    This function will take the arguments, and parsed it accordingly,
    Call the associated arguments module form module.py,
    Raise an error if occurred.
    """
    # Assignment:Argument Handling
    parser = argparse.ArgumentParser(
        description="Python implementation of ls command"
        )
    parser = argparse.ArgumentParser(
        conflict_handler="resolve"
        )
    parser.add_argument(
        'path', 
         nargs='?',
         default='.',
        help="Path to directory"
    )
    parser.add_argument(
        '--dirpath',
        default='data/structure.json',
        help="Path for the directory"
        )
    parser.add_argument(
        '-A',
        action='store_true',
        help="Show hidden files"
        )
    parser.add_argument(
        '-l',
        action='store_true',
        help="Use a long listing format"
        )
    parser.add_argument(
        '-r',
        action='store_true',
        help="Reverse the order of the sort"
        )
    parser.add_argument(
        '-t',
        action='store_true',
        help="Sort by time modified"
        )
    parser.add_argument(
        '--filter',
        help="Filter by file[--filter==file] or directory[--filter==dir]"
        ) #,choices=['file', 'dir']
    parser.add_argument(
        '-h',
        action='store_true',
        help='Print human-readable sizes'
        )
    parser.add_argument(
        "--help", 
        action='help',
        help='Find Help'
        )
    args = parser.parse_args()

    # Assignment:Extract argument
    filepath = args.dirpath
    show_hidden = args.A
    use_long_format = args.l
    reverse_order = args.r
    sort_by_time = args.t
    filter_option = args.filter
    path = args.path
    human_readable = args.h
    
    # Assignment:Load Data
    data = parse_json(filepath)
    #Traverse to Current Directory
    current_directory = handle_path(path,data)
    if current_directory is not None:
        # Linux ls commands
        files = ls(
            current_directory,
            show_hidden,
            use_long_format
            )
        # Display
        display(
            files,
            use_long_format,
            reverse_order,
            sort_by_time,
            filter_option,
            human_readable
            )

if __name__ == "__main__":
    expand()