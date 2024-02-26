import pyautogui
import pygetwindow as gw
import random
import time

# Get the list of all currently open windows
open_windows = gw.getAllTitles()

# Remove any windows that you don't want to switch to (e.g., your code editor)
windows_to_switch = [title for title in open_windows if title != 'YourEditorTitle']

# Check if there are at least 3 windows to switch to
if len(windows_to_switch) < 3:
    print("Not enough windows to switch. Please open at least 3 windows.")
    exit()

# Get the number of hours from the user
try:
    hours = float(input("Enter the number of hours to move the mouse randomly: "))
except ValueError:
    print("Invalid input. Please enter a valid number of hours.")
    exit()

# Calculate the total duration in seconds
total_duration = hours * 3600  # 1 hour = 3600 seconds

# Delay between each movement (in seconds)
movement_delay = 2

# Record the start time
start_time = time.time()

while True:
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Break the loop if the total duration has been reached
    if elapsed_time >= total_duration:
        break

    # Generate a random number to decide how many Alt+Tab actions to perform (1 to 5 times)
    alt_tab_count = random.randint(1, 5)

    # Simulate holding the Alt key
    pyautogui.keyDown('alt')

    for _ in range(alt_tab_count):
        # Simulate pressing the Tab key
        pyautogui.press('tab')
        time.sleep(0.5)  # Sleep briefly to mimic the Tab press

    # Release the Alt key
    pyautogui.keyUp('alt')

    # Sleep briefly to mimic the Alt+Tab switch
    time.sleep(1)

    # Generate random coordinates within the screen boundaries
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Move the mouse to the random coordinates
    pyautogui.moveTo(x, y, duration=0.5)  # Adjust duration as needed

    # Sleep for a while before the next movement
    time.sleep(movement_delay)
