import os
import time
import pyautogui
import pywinctl as pwc

# Constants
icon_folder = "icon"
waiting_time = 3


def wait_for_loading(seconds):
    time.sleep(seconds)


# Specify the Spotify window title
spotify_window_title = "Spotify Premium"  # Adjust this based on your system

# open spotify application
os.system("start spotify")

# wait for spotify to open
wait_for_loading(waiting_time + 1)

# Find the Spotify window
spotify_window = pwc.getWindowsWithTitle(spotify_window_title)[0]

if spotify_window:
    # Bring the Spotify window into focus and maximize it
    spotify_window.activate()
    spotify_window.maximize()
else:
    print(f"Window with title '{spotify_window_title}' not found.")

screen_size = pyautogui.size()
screen_height = screen_size.height

# find your library button
your_library_button = None
try:
    your_library_button = pyautogui.locateCenterOnScreen(
        f"{icon_folder}/your_library_expanded.png")
except pyautogui.ImageNotFoundException:
    your_library_button = pyautogui.locateCenterOnScreen(
        f"{icon_folder}/your_library_collapsed.png")

# move cursor to library section and scroll to the top of library
pyautogui.moveTo(your_library_button)
pyautogui.move(0, screen_height*0.2)
pyautogui.scroll(screen_height)

# find your episodes button
your_episodes_button = pyautogui.locateCenterOnScreen(
    f"{icon_folder}/your_episodes.png")
pyautogui.moveTo(your_episodes_button)

# open your episodes
pyautogui.click()

# wait for your episodes to load
wait_for_loading(waiting_time)

# find play button
#   the add button does not appear while the cursor is else where,
#   so we need to move the cursor on top of the episode
play_button = pyautogui.locateCenterOnScreen(f"{icon_folder}/play.png")
pyautogui.moveTo(play_button)
pyautogui.move(0, screen_height*0.2)

# delete all episodes in your episodes
count = 0
while True:
    try:
        add_button = pyautogui.locateCenterOnScreen(f"{icon_folder}/added.png")
        pyautogui.moveTo(add_button)
        pyautogui.click()
        # while the cursor is on the add button, the button becomes a little bigger,
        #   making the search of the add button failure. I choose to move the cursor
        #   a little bit higher(instead of searching for the enlarged button), so that
        #   the add button remains visible and the size is also the same
        pyautogui.move(0, screen_height*(-0.05))
        count = count + 1
    except pyautogui.ImageNotFoundException:
        print("No episodes left")
        break
print(f"delete {count} episodes")
