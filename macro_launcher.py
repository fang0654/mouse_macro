#!/usr/bin/python

import json
from evdev import InputDevice, categorize, ecodes
from subprocess import Popen
import sys

if len(sys.argv) == 2:
    debug = True
else:
    debug = False
device = InputDevice("/dev/input/by-id/usb-Razer_Razer_Naga_Trinity_00000000001A-if02-event-kbd")
device.grab()

macros = json.loads(open('/home/danny/.macros/config.json').read())

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

