import os
from enum import Enum
import inspect
import pkgutil
import importlib
import re

class Section(Enum):
    NONE = None
    DESCRIPTION = '"""'
    PARAMETERS = 'Parameters'
    RETURNS = 'Returns'

def is_class(line:str):
    return 'class' in line

def is_method(line:str):
    return 'def' in line

def get_name(line:str):
    line = line.replace(' ', '')
    if is_class(line):
        s_i = line.find('class')
        e_i = line.find('(')

def generate_file(base_module:str, number:str, modulename:str, filename:str):
    README = ''
    module = importlib.import_module(modulename)
    for name, sub_module in module.__dict__.items():
        if name.startswith('__'):
            continue
        if not hasattr(sub_module, '__package__'):
            continue
        if not sub_module.__package__.startswith(base_module):
            continue

        constants = ''
        nr = 1
        for member_name, obj in inspect.getmembers(sub_module):
            if hasattr(obj, '__module__') and not obj.__module__.startswith(base_module):
                continue
            if hasattr(obj, '__package__') and not obj.__package__.startswith(base_module):
                continue
            if member_name.startswith('__'):
                continue
            if hasattr(obj, '__name__') and obj.__name__.startswith('__'):
                continue
            if inspect.isclass(obj):
                README += generate_class(base_module, f'{number}.{nr}', obj)
                nr += 1
            elif inspect.ismethod(obj) or inspect.isfunction(obj):
                README += generate_function(base_module, f'{number}.{nr}', obj)
                nr += 1
            else:
                if constants == '':
                    constants += '| Name | Value | Description |\n'
                    constants += '| -----|-------|------------ |\n'
                with open(sub_module.__file__) as f:
                    const_desc = ''
                    lines = f.readlines()
                    for line in lines:
                        if not member_name in line:
                            continue
                        const_desc_start = line.find('#')
                        if const_desc_start == -1:
                            break
                        const_desc_start += 1
                        const_desc += line[const_desc_start:]
                        while const_desc[0] == ' ':
                            const_desc = const_desc[1:]
                        const_desc = const_desc.replace('\n', '')
                        break
                constants += f'| {member_name} | {obj} | {const_desc} |\n'
                
                pass
        
        if constants != '':
            README = f'{constants}\n\n' + README
            #README = '**Constants**\n\n' + README
            README = generate_headline(base_module, f'{number}.{nr}', f'{number}.{nr}.Constants') + README
            nr += 1
        README = generate_headline(base_module, number, sub_module.__name__) + README

        if inspect.isclass(sub_module):
            pass
        pass
    test = __import__(modulename, filename)
    return README

def generate_class(base_module:str, number:str, obj):
    README = generate_headline(base_module, number, f'{obj.__module__}.{obj.__name__}')
    doc = inspect.getdoc(obj)

    if doc is not None:
        README += '**Description**\n\n'
        README += f'{doc}\n\n'

    nr = 1
    for member_name, member in inspect.getmembers(obj):
        if member_name.startswith('__') and member_name not in ['__init__', '__call__']:
            continue
        if inspect.isroutine(member):
            README += generate_function(base_module, f'{number}.{nr}', member)
            nr += 1
            pass
        pass

    return README

def generate_constant(number:str, name:str, obj):
    README = ''
    README += generate_headline('', number, name)

    return README

def generate_function(base_module:str, number:str, obj):
    README = ''
    doc = inspect.getdoc(obj)
    comments = inspect.getcomments(obj)
    
    README += generate_headline(base_module, number, f'{obj.__module__}.{obj.__qualname__}')
    README += '**Description**\n\n'

    section = Section.DESCRIPTION
    if doc is not None:
        lines = doc.split('\n')

        i = 0
        while i < len(lines):
            line = lines[i]
            if Section.PARAMETERS.value in line and lines[i+1].startswith('--'):
                section = Section.PARAMETERS
                README += '**Parameters**\n\n'
                README += '| Name | Type | Description |\n'
                README += '|------|------|-------------|\n'
                i += 2
                continue
            elif Section.RETURNS.value in line and lines[i+1].startswith('--'):
                section = Section.RETURNS
                README += '\n**Returns**\n\n'
                i += 2
                continue

            if line == '':
                i += 1
                continue
            
            if section == Section.DESCRIPTION:
                README += f'{line}\n\n'
            elif section == Section.PARAMETERS:
                start_name = 0
                end_name = line.find(':')
                start_type = end_name + 1
                end_type = len(line)
                p_name = line[start_name:end_name].replace(' ', '')
                p_type = line[start_type:end_type]#.replace(' ', '')
                while p_type[0] == ' ':
                    p_type = p_type[1:]

                i += 1
                line = lines[i]
                while line[0] == ' ':
                    line = line[1:]
                p_desc = line
                
                README += f'| {p_name} | {p_type} | {p_desc} |\n'
            elif section == Section.RETURNS:
                r_type = line
                i += 1
                r_name = lines[i]
                while r_name[0] == ' ':
                    r_name = r_name[1:]
                README += f'{r_name} : {r_type}\n\n'
            i += 1

    if comments is not None:
        comments = comments.replace('#', '')
        comments = comments.replace('\\t', '\t')
        equations = ''
        examples = ''
        images = ''
        lines = comments.split('\n')
        for line in lines:
            if '__equation__' in line:
                line = line.replace('__equation__', '')
                while line[0] == ' ':
                    line = line[1:]
                equations += f'{line}\n\n'
            elif '__example__' in line:
                line = line.replace('__example__', '')
                while len(line) > 0 and line[0] == ' ':
                    line = line[1:]
                line = line.replace('\t', '  ')
                line = line.replace('\\n', '\n')
                if examples == '':
                    examples += '```python\n'
                for sub_line in line.split('\n'):
                    examples += f'{sub_line}\n'
            elif '__image__' in line:
                line = line.replace('__image__', '')
                while len(line) > 0 and line[0] == ' ':
                    line = line[1:]
                images += f'{line}\n'

        if equations != '':
            README += '**Equations**\n\n'
            README += f'{equations}\n\n'
        if examples != '':
            examples += '```'
            README += '**Example**\n\n'
            README += f'{examples}\n\n'
        README += images
        pass

    return README

def generate_headline(base_module:str, number:str, name):
    name = name.replace(f'{base_module}.', '')
    name = name.replace('_', '\_')
    README = ''
    parts = name.split('.')
    level = len(parts) - 1
    for i in range(level):
        README += '#'
    README += f' {number} {parts[-1]}\n\n'
    README += '[TOC](#table-of-contents)\n\n'
    return README

def generate_sub_module(base_module:str, number:str, module_name:str):
    #test = importlib.import_module(module_name)

    module_dir = module_name.replace('.', '/')

    README = ''
    nr = 1

    entries = sorted(os.listdir(module_dir))
    if not '__init__.py' in entries:
        return README
    
    for entry in entries:
        if entry.startswith('__'):
            continue
        if entry.endswith('.py'):
            sub_number = number

            README += generate_file(base_module, sub_number, module_name, entry)
            nr += 1
        elif os.path.isdir(f'{module_dir}/{entry}'):
            sub_number = str(nr) if number is None else f'{number}.{nr}'
            README += generate_sub_module(base_module, sub_number, f'{module_name}.{entry}')
            nr += 1
        pass
    
    return README

def generate_TOC(README):
    TOC = '# Table of Contents\n\n'
    for line in README.split('\n'):
        if not '#' in line:
            continue
        if '#table-of-contents' in line:
            continue
        line = line[1:]
        while line[0] == '#':
            TOC += '  '
            line = line[1:]
        line = line[1:]
        TOC += f'- [{line}]'
        line = line.replace(' ', '-')
        line = line.replace('.', '')
        line = line.lower()
        TOC += f'(#{line})\n'
        pass
    TOC += '\n\n'
    return TOC

if __name__ == '__main__':
    OUT_FILE = 'README.md'

    README = generate_sub_module('rsp.ml', None, 'rsp.ml')

    TOC = generate_TOC(README)
    README = TOC + README

    with open(OUT_FILE, 'w') as f:
        f.write(README)
    pass