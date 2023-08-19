import os

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

def main():
    """Finding and cleaning project files"""

    print(f'Current directory path: {os.path.dirname(__file__)}')

    filename = 'some.c'

    removed_lines = clear_file(filename)
    if removed_lines:
        print(f'From {filename} removed {removed_lines} lines')

if __name__ == '__main__':
    main()
