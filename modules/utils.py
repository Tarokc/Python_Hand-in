import os


def get_file_names(folderpath, out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    items = os.listdir(folderpath)
    with open(out, 'w') as output:
        for item in items:
            output.write(str(item) + "\n")


def get_all_file_names(folderpath, out='output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    with open(out, 'w') as output:
        for root, directories, files in os.walk(folderpath):
            directories[:] = [d for d in directories if d not in [
                '.git'] not in ['.ipynb_checkpoints']]
            for filename in files:
                output.write(os.path.join(root, filename) + "\n")


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""


def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""


def write_headlines(md_files, out='output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
