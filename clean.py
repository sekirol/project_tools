import os

FILES_FOR_CLEAN_EXTENTIONS = ('.c', '.h')

TEMP_FILE_EXTENTION = ".temp"
LINE_FOR_REMOVE_TEMPLATE = "/* USER CODE "

def clean_file(file_path):
    """Removes lines that contain pattern"""
    temp_file_path = file_path + TEMP_FILE_EXTENTION
    f_temp = open(temp_file_path, 'w', encoding='UTF-8')

    lines_counter = 0
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            if line.find(LINE_FOR_REMOVE_TEMPLATE) != -1:
                lines_counter += 1
                continue

            f_temp.write(f'{line}')

    f_temp.close()

    os.remove(file_path)
    os.rename(temp_file_path, file_path)

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
    
    modified_files = 0
    for file_path in files:
        removed_lines = clean_file(file_path)
        if removed_lines:
            print(f'From {file_path} removed {removed_lines} lines')
            modified_files += 1

    if modified_files:
        print(f'Modified {modified_files} files in project')
    else:
        print(f'Nothing to modify in project')

if __name__ == '__main__':
    main()
