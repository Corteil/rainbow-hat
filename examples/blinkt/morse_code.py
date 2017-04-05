#!/usr/bin/env python

import time

import rainbowhat

set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit
set_pixel=rainbowhat.rainbow.set_pixel
show=rainbowhat.rainbow.show

set_clear_on_exit()

def show_all(state):
    for i in range(7):
        val = state * 255
        set_pixel(i, val, val, val)
    show()

def dot():
    show_all(1)
    time.sleep(0.05)
    show_all(0)
    time.sleep(0.2)

def dash():
    show_all(1)
    time.sleep(0.2)
    show_all(0)
    time.sleep(0.2)

def space():
    time.sleep(0.2)

#0 is a space, 1 is a dot and 2 is a dash
morse = '211101101211022101020120210212000'

while True:
    for m in morse:
        if m == '0':
            space()
        elif m == '1':
            dot()
        elif m == '2':
            dash()
