from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = "templates/"
TEMPLATE_NAME = "base.txt"

separators = ['HELLO', 'WORLD', 'HOW', 'ARE', 'YOU']

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template(TEMPLATE_NAME)

def generate_file(filename):
    context = {
        'filename': filename,
        'author': 'Sergei Kirikeza',
        'description': 'This is short description of module',
        'separators': separators
    }

    generated = template.render(**context)
    with open(filename, 'x', encoding='utf-8') as f:
        f.write(generated)

def main():
    files = ['test.c', 'test.h']

    for filename in files:
        try:
            generate_file(filename)
            print(f'File {filename} was generated')
        
        except FileExistsError:
            print(f'File {filename} already exists')

if __name__ == '__main__':
    main()