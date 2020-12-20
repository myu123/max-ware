from multiprocessing import Process
import glow, no_flash, trigger

if __name__ == '__main__':
    p1 = Process(target = glow.glow)
    p1.start()
    p2 = Process(target = no_flash.no_flash)
    p2.start()
    p3 = Process(target = trigger.trigger)
    p3.start()