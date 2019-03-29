#!/usr/bin/python

import json
from evdev import InputDevice, categorize, ecodes
from subprocess import Popen
import sys
import os

config_path = os.path.join(os.getenv("HOME"), ".macros/config.json")
if len(sys.argv) == 2:
    debug = True
else:
    debug = False
devices = os.listdir('/dev/input/by-id/')

nagas = [os.path.join('/dev/input/by-id/',d) for d in devices if 'usb-Razer_Razer_Naga' in d and 'if02-event-kbd' in d]
if len(nagas) == 0:
    print("No Naga devices found. :(")
    sys.exit(1)


device = InputDevice(nagas[0])

device.grab()

macros = json.loads(open(config_path).read())

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            k = str(event.code-1)
            if debug:
                print("Keypress captured: {}".format(k))
            if macros.get(k, False):
                if debug:
                    print("Macro being executed: {}".format(macros[k]))
                Popen(macros[k], shell=True)

