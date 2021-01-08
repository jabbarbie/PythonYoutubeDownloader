
import time, sys
import itertools
import threading

global done
done = False
def test_animasi():
    for i in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rPlease Wait' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!           ')

def animasi():
    t = threading.Thread(target=test_animasi)
    t.start()        


#long process here
animasi()
time.sleep(10)
done = True