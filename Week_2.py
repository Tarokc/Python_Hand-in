from modules import file_handler
from modules import webget
import argparse
from modules import utils

# Exercise 1
# 1_A

#url = 'https://docs.google.com/uc?export=download&id=1W3Yb8Fr8WA8yU6zjjsvPJ8D1h_LYDzIL'
# webget.download(url)

# file_handler.print_file_content('Sample100.csv')


# 1_B
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#file_handler.write_list_to_file('output.txt', 'lst', 'hello', 'hej', 'goddav!')


# 1_C
#content = file_handler.read_csv('Sample100.csv')
# for item in content:
# print(item.strip())


# 2_A
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='CSV file writer')
#     parser.add_argument('path', help='Add the path to a file to be read')
#     parser.add_argument('-f', '--file', help="Name of file to save as")

#     args = parser.parse_args()
#     if args.file == None:
#         print("Input file:", args.path)
#         file_handler.print_file_content(args.path)
#     else:
#         file_handler.write_list_to_file(
#             args.file, file_handler.read_csv(args.path))
#         print("Input file:", args.path)
#         print("Output file:", args.file)

path = "..\\Python_Hand-in"
#utils.get_file_names(path, 'folder_filenames.txt')
utils.get_all_file_names(path)
