#!/usr/bin/env python

import threading
import time


def worker():
    print("i'm thread")
    t = threading.current_thread()
    time.sleep(8)
    print(t.name)


#new_t = threading.Thread(target=worker, name='sjk_thread')
#new_t.start()
worker()

t = threading.current_thread()
print(t.name)
