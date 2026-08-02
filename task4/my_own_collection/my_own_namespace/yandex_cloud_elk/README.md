# Ansible Collection - my_own_namespace.yandex_cloud_elk

Учебная коллекция Ansible для создания файлов и развёртывания стека Observability.

## Возможности

| Компонент | Назначение |
|---|---|
| `my_own_module` | Создаёт текстовый файл по указанному пути с указанным содержимым |
| `file_creator` | Роль-обёртка для модуля со значениями по умолчанию |

## Параметры модуля

| Параметр | Тип | Обязательный | Описание |
|---|---|---|---|
| `path` | `str` | Да | Путь к создаваемому файлу |
| `content` | `str` | Да | Содержимое файла |

## Установка

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

## Пример playbook

```yaml
---
- name: Test collection
  hosts: localhost
  connection: local
  roles:
    - role: my_own_namespace.yandex_cloud_elk.file_creator
      vars:
        file_path: /tmp/my_file.txt
        file_content: "Содержимое файла"
```
