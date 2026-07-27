lighthouse-role
==============

Устанавливает и настраивает [LightHouse](https://github.com/VKCOM/lighthouse) — веб-интерфейс для СУБД ClickHouse.

## Требования

- ОС: Ubuntu 20.04+, Debian 11+
- Ansible 2.10+

## Переменные

| Переменная | Описание | Значение по умолчанию |
|---|---|---|
| `lighthouse_version` | Версия LightHouse (ветка) | `master` |
| `lighthouse_url` | URL архива для скачивания | `https://github.com/VKCOM/lighthouse/archive/refs/heads/master.zip` |
| `lighthouse_dest` | Директория установки | `/var/www/lighthouse` |

## Зависимости

Нет.

## Пример playbook

```yaml
- name: Install Lighthouse
  hosts: lighthouse
  become: true
  roles:
    - lighthouse-role
```

## Лицензия

MIT

## Автор

Gureev Eugene (iGureEV)
