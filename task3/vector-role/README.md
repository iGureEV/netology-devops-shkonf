vector-role
============

Устанавливает и настраивает [Vector](https://vector.dev/) — инструмент для сбора и маршрутизации логов.

## Требования

- ОС: Ubuntu 20.04+, Debian 11+
- Ansible 2.10+

## Переменные

| Переменная | Описание | Значение по умолчанию |
|---|---|---|
| `vector_version` | Версия Vector | `0.34.1` |
| `vector_arch` | Архитектура | `amd64` |
| `vector_deb_url` | URL deb-пакета | `https://packages.timber.io/vector/...` |

## Зависимости

Нет.

## Пример playbook

```yaml
- name: Install Vector
  hosts: vector
  become: true
  roles:
    - vector-role
```

## Лицензия

MIT

## Автор

Gureev Eugene (iGureEV)
