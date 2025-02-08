import pyautogui
import cv2
import numpy as np
import time

button_image_path = '../nexus_mod_slow_download_autoclick/button.jpg'

confidence_threshold = 0.8

def find_button_on_screen(confidence=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    button_image = cv2.imread(button_image_path, cv2.IMREAD_COLOR)

    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        button_width = button_image.shape[1]
        button_height = button_image.shape[0]
        button_center_x = max_loc[0] + button_width // 2
        button_center_y = max_loc[1] + button_height // 2
        return button_center_x, button_center_y
    else:
        return None

def click_button(button_position):
    if button_position:
        x, y = button_position
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click()
        print(f"Button clicked at ({x}, {y})")
    else:
        print("Button not found on the screen.")

def main():
    print("Where are you, button?")
    while True:
        button_position = find_button_on_screen(confidence_threshold)

        if button_position:
            click_button(button_position)

        time.sleep(1)

if __name__ == "__main__":
    main()