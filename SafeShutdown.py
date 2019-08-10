#!/usr/bin/env python3
from gpiozero import Button, LED
import os 
from signal import pause

powerPin = 3 
resetPin = 2 
ledPin = 14 
powerenPin = 4 
hold = 1

led = LED(ledPin)
led.on()

power = LED(powerenPin)
power.on()

#functions that handle button events
def pressed_power():
  led.blink(.2,.2)
  os.system("sleep 5s && sudo shutdown -h now")

def pressed_reset(): 
  led.blink(.2,.2)
  os.system("sleep 5s && sudo shutdown -r now")

def released_button():
  led.on()
  
powerBtn = Button(powerPin, hold_time=hold)
powerBtn.when_pressed = pressed_power
powerBtn.when_released = released_button

resetBtn = Button(resetPin, hold_time=hold)
resetBtn.when_pressed = pressed_reset 
resetBtn.when_released = released_button

pause()
