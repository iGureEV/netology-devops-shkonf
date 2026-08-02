#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file on a remote host

version_added: "1.0.0"

description:
    - This module creates a text file at a specified path with specified content on remote hosts.
    - It is idempotent, meaning it will not modify the file if it already exists with the desired content.

options:
    path:
        description: The absolute path on the remote host where the file should be created.
        required: true
        type: str
    content:
        description: The text content to be written to the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Create a simple file
- name: Create a test file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test_file.txt
    content: "Hello Ansible!"

# Ensure a config file has specific content
- name: Create a config file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /etc/myapp.conf
    content: |
      [Section]
      key = value
'''

RETURN = r'''
path:
    description: The path of the created file.
    type: str
    returned: always
    sample: '/tmp/test_file.txt'
content:
    description: The content written to the file.
    type: str
    returned: always
    sample: 'Hello Ansible!'
message:
    description: A status message describing what happened.
    type: str
    returned: always
    sample: 'File created successfully'
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    # Определяем аргументы, которые принимает модуль
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # Инициализируем результат
    result = dict(
        changed=False,
        path='',
        content='',
        message=''
    )

    # Создаём объект AnsibleModule
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path

    # Создаём директорию для файла, если её нет
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            module.fail_json(msg=f'Failed to create directory {directory}: {str(e)}', **result)

    # Проверяем, существует ли файл, и совпадает ли его содержимое
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                existing_content = f.read()
            if existing_content == content:
                # Файл уже существует с нужным содержимым. Изменений нет.
                result['content'] = content
                result['message'] = 'File already exists with desired content. No changes made.'
                module.exit_json(**result)
        except IOError as e:
            module.fail_json(msg=f'Failed to read file {path}: {str(e)}', **result)

    # Если мы здесь, значит файл либо не существует, либо содержимое отличается.
    # Меняем статус changed на True
    result['changed'] = True
    result['content'] = content

    # Если режим проверки (--check), не вносим реальных изменений
    if module.check_mode:
        result['message'] = 'File would be created/updated.'
        module.exit_json(**result)

    # Пытаемся записать файл
    try:
        with open(path, 'w') as f:
            f.write(content)
        result['message'] = 'File created/updated successfully.'
    except IOError as e:
        module.fail_json(msg=f'Failed to write to file {path}: {str(e)}', **result)

    # Успешное завершение с изменениями
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
