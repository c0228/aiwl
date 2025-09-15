import pyautogui
import time

def move(x, y):
    """
    Moves the mouse to (x, y) and clicks.
    
    :param x: X coordinate
    :param y: Y coordinate
    :param clicks: Number of clicks
    :param interval: Delay between clicks
    :param button: 'left' or 'right'
    """
    pyautogui.moveTo(x, y, duration=0.5)  # move smoothly in 0.5 seconds

def click(clicks=1, interval=0.25, button='left'):
    """
    Moves the mouse to (x, y) and clicks.
    
    :param x: X coordinate
    :param y: Y coordinate
    :param clicks: Number of clicks
    :param interval: Delay between clicks
    :param button: 'left' or 'right'
    """
    pyautogui.click(clicks=clicks, interval=interval, button=button)

def open_desktop_app(app_icon_coords):
    """
    Selects and opens a desktop app given its icon coordinates.
    
    :param app_icon_coords: Tuple of (x, y) coordinates of the app icon
    """
    move(*app_icon_coords)
    time.sleep(0.2)  # wait for app to open

if __name__ == "__main__":
    # Example: move mouse to Notepad icon at (200, 500) and open it
    app_coords1 = (200, 500)  
    open_desktop_app(app_coords1)
    app_coords2 = (600, 400)  
    open_desktop_app(app_coords2)
    click()
