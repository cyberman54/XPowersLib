'''
@license MIT License

Copyright (c) 2022 lewis he

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@file      AXP192_GpioInput.py
@author    Lewis He (lewishe@outlook.com)
@date      2022-10-20

'''
from AXP192 import *
import time

SDA = None
SCL = None

if implementation.name == 'micropython':
    SDA = 21
    SCL = 22
if implementation.name == 'circuitpython':
    from board import *
    SDA = IO15
    SCL = IO7


PMU = AXP192(addr=AXP192_SLAVE_ADDRESS,sda=SDA, scl=SCL)

id = PMU.getChipID()
if id != XPOWERS_AXP192_CHIP_ID:
    print("PMU is not online...")
    while True:
        pass

print('getID:%s' % hex(PMU.getChipID()))

PMU.pinMode(PMU_GPIO0,INPUT_PULLDOWN)
PMU.pinMode(PMU_GPIO1,INPUT_PULLDOWN)
PMU.pinMode(PMU_GPIO2,INPUT_PULLDOWN)
PMU.pinMode(PMU_GPIO3,INPUT)
PMU.pinMode(PMU_GPIO4,INPUT)
PMU.pinMode(PMU_GPIO5,INPUT)

print('AXP192 GPIO 3 ~ 5 is a floating input, please ensure there is an external pull-up or pull-down resistor')

while True:
    IO0 = PMU.digitalRead(PMU_GPIO0)
    IO1 = PMU.digitalRead(PMU_GPIO1)
    IO2 = PMU.digitalRead(PMU_GPIO2)
    IO3 = PMU.digitalRead(PMU_GPIO3)
    IO4 = PMU.digitalRead(PMU_GPIO4)
    IO5 = PMU.digitalRead(PMU_GPIO5)
    
    print('IO0:{0} IO1:{1} IO2:{2} IO3:{3} IO4:{4} IO5:{5} '.format(IO0,IO1,IO2,IO3,IO4,IO5))
    
    time.sleep(1.5)
