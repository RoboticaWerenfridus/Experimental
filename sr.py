from gpiozero import Robot
import sys
import tkinter as tk

# Define the robot with the correct motor pins
robot = Robot(left=(18, 17), right=(23, 22))

def key_press(event):
    key = event.char.lower()
    if key == 'w':
        robot.forward()
    elif key == 'a':
        robot.left()
    elif key == 'd':
        robot.right()
    elif key == 's':
        robot.backward()
    elif key == 'q':
        robot.stop()
        sys.exit()

def key_release(event):
    robot.stop()

# Tkinter setup for keyboard input
command = tk.Tk()
command.bind('<KeyPress>', key_press)
command.bind('<KeyRelease>', key_release)
command.mainloop()
