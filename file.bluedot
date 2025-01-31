from gpiozero import Robot
from bluedot import BlueDot
import tkinter as tk

robot = Robot(left=(18, 17), right=(23, 22))

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

def stop():
    robot.stop()

bd.when_pressed = move
bd.when_released = stop
command = tk.Tk()
command.mainloop()
