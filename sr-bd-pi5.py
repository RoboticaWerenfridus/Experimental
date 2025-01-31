# Made by CIB with <3
from gpiozero import Robot, Motor

robot = Robot(left=Motor(17, 18), right=Motor(22, 23))

import sys
import tkinter as tk
from bluedot import BlueDot

bd = BlueDot()

def move(pos):
    if pos.top:
        robot.forward()
    elif pos.left:
        robot.left()
    elif pos.right:
        robot.right()
    elif pos.bottom:
        robot.backward()

def stop1():
    robot.stop()

bd.when_pressed = move
bd.when_released = stop1
command = tk.Tk()
command.mainloop()
