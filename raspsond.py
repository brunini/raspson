#! /bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_jsonrpc import JSONRPC
from RPi import GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pin_board_numbers = [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40]
for bn in pin_board_numbers:
    GPIO.setup(bn, GPIO.OUT)
app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

def check_auth(username, password):
    return True

@jsonrpc.method('index', authenticated=check_auth)
def index():
    return u'Welcome to raspson'

@jsonrpc.method('toggle_output(pin=int) -> int', validate=True, authenticated=check_auth)
def toggle_output(pin):
    if GPIO.input(pin):
        GPIO.output(pin, False) 
        return {u'status': {'output': { 'pins':  { pin: 0 } }  } } 
    else:
        GPIO.output(pin, True)
        return {u'status': {'output': { 'pins':  { pin: 1 } }  } }


@jsonrpc.method('set_output(pin=int, new_state=int) -> int', validate=True, authenticated=check_auth)
def set_output(pin, new_state):
    GPIO.output(pin, new_state) 
    return {u'status': {'output': { 'pins':  { pin: new_state } }  } } 


@jsonrpc.method('get_status(pin=int) -> int', validate=True, authenticated=check_auth)
def get_status(pin):
    return {u'status': {'output': { 'pins':  { pin: GPIO.input(pin) } }  } } 


@jsonrpc.method('get_all_status(pin=int) -> int', validate=True, authenticated=check_auth)
def get_status(pin):
    pin_status = {}
    for pin in pin_board_numbers:
        pin_status[pin] = GPIO.input(pin)
    return {u'status': {'output': { 'pins':  pin_status }  } } 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
