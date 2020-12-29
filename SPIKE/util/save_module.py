# EOF


import os
import sys


TARGET_MODULE_NAME = '___'

# set target file path in projects/ directory
target_file_path = 'projects/{}.py'.format(TARGET_MODULE_NAME)

# save current file to target file
print('SAVING {} AS {}...'.format(__file__, target_file_path))
os.rename(__file__, target_file_path)

# remove file content after "# EOF"
with open(target_file_path, 'r') as f:
    file_content = f.read()
file_content = file_content.split('# EOF')[0]
with open(target_file_path, 'w') as f:
    f.write(file_content)

# list projects/ directory and print file content before exiting
print(os.listdir('projects'))
print('{} SAVED:\n```\n{}\n```'.format(target_file_path, file_content))
sys.exit()
