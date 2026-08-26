#!/usr/bin/env python3

import logging
import random
import time
import json

while True:
    number = random.randrange(0, 4)

    if number == 0:
        level = 'info'
        msg = 'Hello there!!'
    elif number == 1:
        level = 'warning'
        msg = 'Hmmm....something strange'
    elif number == 2:
        level = 'error'
        msg = 'OH NO!!!!!!'
    elif number == 3:
        level = 'exception'
        msg = 'this is exception'

    # Выводим JSON-строку в stdout
    print(json.dumps({'level': level, 'message': msg}))
    time.sleep(1)
