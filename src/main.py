"""
Created by hatuongnguyen on 13:31:31 - 3/24/24

Project: BiKipTramTrieu
Path: BiKipTramTrieu/src
"""

import string
import time

slogan: string = 'Welcome to our multilevel team, you will be a billionaire if you join our team!'


def printSlow(text: string, delay: float = 0.02):
    temp = ''
    for char in text:
        if char in string.printable:
            temp += ('\033[92;1m' + char + '\033[0m')
            print(temp, end='\r')
            time.sleep(delay)


def printALot(text: string, delay: float = 0.005):
    temp = ''
    for char in text:
        for i in string.printable:
            if i == char or char == ' ':
                time.sleep(delay)
                print(temp + '\033[91;1m' + i + '\033[0m')
                temp += ('\033[92;1m' + char + '\033[0m')
                break
            else:
                time.sleep(delay)
                print(temp + '\033[91;1m' + i + '\033[0m')


printALot(slogan)
printSlow(slogan)
