import os

FILES_FOR_CLEAN_EXTENTIONS = ('.c', '.h')

TEMP_FILE_PREFIX = "temp_"
LINE_FOR_REMOVE_TEMPLATE = "/* USER CODE "

def clear_file(filename):
    temp_file_name = TEMP_FILE_PREFIX + filename 
    f_temp = open(temp_file_name, 'w', encoding='UTF-8')
    
    lines_counter = 0
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            if line.find(LINE_FOR_REMOVE_TEMPLATE) != -1:
                lines_counter += 1
                continue

            f_temp.write(f'{line}')

    f_temp.close()

    os.remove(filename)
    os.rename(temp_file_name, filename)

    return lines_counter

def get_files_for_clean(generic_path):
    """Returns file paths to clean up"""
    paths = []
    for root, dirs, files in os.walk(generic_path):
        for file in files:
            extension = os.path.splitext(file)[1]
            if extension in FILES_FOR_CLEAN_EXTENTIONS:
                paths.append(os.path.join(root, file))

    return paths

def main():
    """Finding and cleaning project files"""

    generic_path = os.path.dirname(__file__)
    print(f'Current directory path: {generic_path}')

    files = get_files_for_clean(generic_path)
    for path in files:
        print(path)

    filename = 'some.c'

    removed_lines = clear_file(filename)
    if removed_lines:
        print(f'From {filename} removed {removed_lines} lines')

if __name__ == '__main__':
    main()
