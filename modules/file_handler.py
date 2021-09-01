def print_file_content(file):
    with open(file) as file:
        content = file.read()
    print(content)


def write_list_to_file(output_file, *strings):
    with open(output_file, 'w') as file:
        for item in strings:
            if type(item) == list:
                for list_item in item:
                    file.write(str(list_item.strip().split('\n')) + '\n')
            file.write(str(item) + '\n')


def read_csv(file):
    with open(file) as file:
        content = file.readlines()
        return [item for item in content]
