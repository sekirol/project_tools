import sys
import json

from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = "templates/"
TEMPLATE_NAME = "base.txt"
INFO_FILE_NAME = "config.json"

FILE_TYPES = (
    ('source', '.c'),
    ('header', '.h')
)

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

env.trim_blocks = True
env.lstrip_blocks = True

template = env.get_template(TEMPLATE_NAME)

def generate_file(file_name, info, file_type):
    separators = info.get('separators') or []
    context = {
        'filename': file_name,
        'author': info.get('author_name') or "",
        'description': info.get('description_template') or "",
        'separators': separators.get(file_type) or [],
        'include_guard': file_name.replace('.', '_').upper() \
            if file_type == 'header' else "",
        'include_header': file_name.replace('.c', '.h') \
            if file_type == 'source' else ""
    }

    generated = template.render(**context)
    with open(file_name, 'x', encoding='utf-8') as f:
        f.write(generated)

def main():
    module_names = sys.argv[1:]
    if not module_names:
        print(f'Module name not specified')
        return
    
    files = [(f'{name}{extention}', file_type)
             for name in module_names
             for file_type, extention in FILE_TYPES]

    # TODO: Information file verification function
    # TODO: Checking for separator 'includes'
    with open(INFO_FILE_NAME, 'r', encoding='utf-8') as f:
        info = json.load(f)

    for file_name, flie_type in files:
        try:
            generate_file(file_name, info, flie_type)
            print(f'File {file_name} was generated')
        
        except FileExistsError:
            print(f'File {file_name} already exists')

if __name__ == '__main__':
    main()