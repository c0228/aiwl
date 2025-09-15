import pyautogui
import time

from mouseMove import move, click  # import your existing functions

def minimizeDesktop():
    # Minimize all windows to show desktop
    print("Minimizing all windows to reveal desktop...")
    pyautogui.hotkey('win', 'd')
    time.sleep(1)  # wait a moment for desktop to appear

def click_icon(icon_image_path, confidence=0.8, wait_time=1):
    """
    Recognizes an icon on the desktop by image and clicks it safely.
    
    :param icon_image_path: Path to the screenshot of the icon (PNG recommended)
    :param confidence: Matching confidence (0.0 - 1.0)
    :param wait_time: Time to wait after clicking
    :return: True if icon found and clicked, False otherwise
    """
    try:
        # Search for the icon on the screen
        location = pyautogui.locateOnScreen(icon_image_path, confidence=confidence)
        
        if location:
            center = pyautogui.center(location)
            move(center.x, center.y)
            click(clicks=2, interval=0.25)  # double-click with 0.25s between clicks
            time.sleep(wait_time)
            return True
        else:
            print(f"Icon '{icon_image_path}' not found on screen!")
            minimizeDesktop()
            
            # Try again after minimizing
            location = pyautogui.locateOnScreen(icon_image_path, confidence=confidence)
            if location:
                center = pyautogui.center(location)
                move(center.x, center.y)
                click(clicks=2, interval=0.25)  # double-click with 0.25s between clicks
                time.sleep(wait_time)
                return True
            else:
                print(f"Still could not find icon '{icon_image_path}' even after minimizing windows.")
                return False

    except pyautogui.ImageNotFoundException:
        print(f"Icon '{icon_image_path}' could not be located (ImageNotFoundException).")
        minimizeDesktop()
        click_icon(icon_image_path, confidence)
        return False
    except Exception as e:
        print(f"An unexpected error occurred while clicking icon: {e}")
        return False

desktopIcons = {
    "AVG Antivirus App": "icons/avg-antivirus.png",
    "Networks": "icons/networks.png",
    "Postman App": "icons/postman.png",
    "Recycle Bin": "icons/recycle-bin.png",
    "This PC Folder": "icons/this-pc.png",
    "Zoom App": "icons/zoom.png",
}
if __name__ == "__main__":
    icon_image_path = desktopIcons["Zoom App"]
    clicked = click_icon(icon_image_path, confidence=0.6)
    
    if clicked:
        print("Notepad icon clicked successfully!")
    else:
        print("Failed to find Notepad icon.")
