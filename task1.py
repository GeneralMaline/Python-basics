from termcolor import colored
import time
class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']
    i = 0
    def running(self):
        if TrafficLight.i == 0:
            print(colored(TrafficLight.__color[TrafficLight.i], 'red'))
            time.sleep(7)
        if TrafficLight.i == 1 or TrafficLight.i == 3:
            print(colored(TrafficLight.__color[TrafficLight.i], 'yellow'))
            time.sleep(2)
        if TrafficLight.i == 2:
            print(colored(TrafficLight.__color[TrafficLight.i], 'green'))
            time.sleep(5)
        TrafficLight.i += 1
        if TrafficLight.i == 4:
            TrafficLight.i = 0

a = TrafficLight()
while True:
    a.running()
