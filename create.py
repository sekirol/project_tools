import json
from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = "templates/"
TEMPLATE_NAME = "base.txt"
INFO_FILE_NAME = "config.json"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template(TEMPLATE_NAME)

def generate_file(filename, info):
    context = {
        'filename': filename,
        'author': info.get('author_name') or "",
        'description': info.get('description_template') or "",
        'separators': info.get('separators') or []
    }

    generated = template.render(**context)
    with open(filename, 'x', encoding='utf-8') as f:
        f.write(generated)

def main():
    files = ['test.c', 'test.h']

    # TODO: Information file verification function
    with open(INFO_FILE_NAME, 'r', encoding='utf-8') as f:
        info = json.load(f)

    for filename in files:
        try:
            generate_file(filename, info)
            print(f'File {filename} was generated')
        
        except FileExistsError:
            print(f'File {filename} already exists')

if __name__ == '__main__':
    main()