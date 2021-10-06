#!/usr/bin/python

import json
from evdev import InputDevice, categorize, ecodes
from subprocess import Popen
import sys
import os
import asyncio
import pdb

async def run_macro(device, macros):
    while True:
        async for event in device.async_read_loop():
            if event.type == ecodes.EV_KEY:
                if event.value == 1:
                    k = str(event.code-1)
                    if debug:
                        print("Keypress captured: {}".format(k))
                    if macros.get(k, False):
                        if debug:
                            print("Macro being executed: {}".format(macros[k]))
                        Popen(macros[k], shell=True)

    

config_path = os.path.join(os.getenv("HOME"), ".macros/config.json")
if len(sys.argv) == 2:
    debug = True
else:
    debug = False
devices = os.listdir('/dev/input/by-id/')

macros = json.loads(open(config_path).read())

mice = [os.path.join('/dev/input/by-id/',d) for d in devices if d in macros.keys()]
# pdb.set_trace()
if len(mice) == 0:
    print("No mouse devices with configured profiles found. :(")
    sys.exit(1)


devices = [[InputDevice(m), macros[m.split('/')[-1]]] for m in mice]

for device, m in devices:
    device.grab()
    # pdb.set_trace()
    asyncio.ensure_future(run_macro(device, m))

loop = asyncio.get_event_loop()
loop.run_forever()



# for event in device.read_loop():
#     if event.type == ecodes.EV_KEY:
#         if event.value == 1:
#             k = str(event.code-1)
#             if debug:
#                 print("Keypress captured: {}".format(k))
#             if macros.get(k, False):
#                 if debug:
#                     print("Macro being executed: {}".format(macros[k]))
#                 Popen(macros[k], shell=True)

