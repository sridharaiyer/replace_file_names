import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--dirname", action="store", help='Directory of the files which have to be renamed')
parser.add_argument("--suffix", action="store", default=None, help='Suffix a string to the file names')
args = parser.parse_args()

if not os.path.isdir(args.dirname):
    print('{} not a valid directory. Exiting the program.'.format(args.dirname))
    exit(1)


remove_strings = [
    'Margazhi_Utsavam',
    'On_Monday',
    'On_Tuesday',
    'On_Wednesday',
    'On_Thursday',
    'On_Friday',
    'On_Saturday',
    'On_Sunday'
]

replace_strings_dict = dict.fromkeys(remove_strings, '')

robj = re.compile('|'.join(replace_strings_dict.keys()))

regex = re.compile('[^a-zA-Z0-9]')

paths = (os.path.join(root, filename)
         for root, _, filenames in os.walk(args.dirname)
         for filename in filenames)

for path in paths:
    file_name = robj.sub(lambda m: replace_strings_dict[m.group(0)], os.path.basename(path))
    file_name, extension = os.path.splitext(file_name)
    file_name = regex.sub('', file_name)
    if args.suffix is None or args.suffix.strip() == '':
        file_name = file_name + extension
    else:
        file_name = args.suffix + '_' + file_name + extension

    newname = os.path.join(os.path.dirname(path), file_name)

    if newname != path:
        os.rename(path, newname)
