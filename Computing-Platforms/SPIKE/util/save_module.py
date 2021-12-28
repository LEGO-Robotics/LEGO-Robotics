# ref: https://stackoverflow.com/questions/64449448/how-to-import-from-custom-python-modules-on-new-lego-mindstorms-robot-inventor


# EOF


import os
import sys


TARGET_FILE_NAME = '___.py'


# save current file to target file
print('SAVING {} AS {}...'.format(__file__, TARGET_FILE_NAME))
os.rename(__file__, TARGET_FILE_NAME)

# remove file content after "# EOF"
with open(TARGET_FILE_NAME, 'r') as f:
    file_content = f.read()
file_content = file_content.split('# EOF')[0]
with open(TARGET_FILE_NAME, 'w') as f:
    f.write(file_content)

# list projects/ directory and print file content before exiting
print(os.listdir())
print('{} SAVED:\n```\n{}\n```'.format(TARGET_FILE_NAME, file_content))
sys.exit()
