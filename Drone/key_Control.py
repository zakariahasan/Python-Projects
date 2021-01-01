from djitellopy import tello
import keboard as kp
from time import sleep

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def geKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getkey('LEFT'): lr = speed
    elif kp.getkey('RIGHT'): lr = -speed
    if kp.getkey('UP'): fb = -speed
    elif kp.getkey('DOWN'): fb =  speed
    if kp.getkey('w'): ud = speed
    elif kp.getkey('s'): ud = - speed
    if kp.getkey('a'): yv = speed
    elif kp.getkey('d'): yv = - speed

    if kp.getkey('q'): drone.land(); sleep(3)
    if kp.getkey('t'): drone.takeoff()
    return [lr, fb, ud, yv]

while True:
    vals = geKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
