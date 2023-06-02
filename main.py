import sys

import screen_ocr
import pyautogui
import time


def start_fishing():
    pyautogui.keyDown('E')
    time.sleep(2)
    pyautogui.keyUp('E')


def trim_message(fish_message):
    return fish_message.replace(" ", "").lower()


if __name__ == '__main__':
    debug = False
    if len(sys.argv) > 1 and sys.argv[1] == '--debug':
        print("[DEBUG] On")
        debug = True

    x, y = pyautogui.size()

    # Those are coordinates of the interaction box containing fishing related messages
    # This script reads messages from the box using OCR
    box_x1 = int(x * 0.400)
    box_x2 = int(x * 0.600)
    box_y1 = int(y * 0.625)
    box_y2 = int(y * 0.725)
    
    if debug:
        print(f"[DEBUG] OCR box coordinates: {box_x1}, {box_x2}, {box_y1}, {box_y2}")
    
    ocr_reader = screen_ocr.Reader.create_quality_reader()
    while True:
        results = ocr_reader.read_screen(bounding_box=(box_x1, box_y1, box_x2, box_y2)).as_string()

        if debug:
            print(f"[DEBUG] pond wait input: {results}")

        if "fishing" in trim_message(results):
            print("Pond detected. Launching loop")

            time.sleep(2)

            break

        print("Waiting for you to approach the fishing pond!")

        time.sleep(1)

    start_fishing()

    # Start fishing loop
    while True:
        results = ocr_reader.read_screen(bounding_box=(box_x1, box_y1, box_x2, box_y2)).as_string()

        if debug:
            print(f"[DEBUG] pond catch input: {results}")

        trimmed_message = trim_message(results)

        if "catch" in trimmed_message:
            print("Fish Caught!")
            pyautogui.keyDown('E')
            time.sleep(0.1)
            pyautogui.keyUp('E')

            # Wait for the animation
            time.sleep(3)

            # And restart fishing
            start_fishing()

        elif "fishing" in trimmed_message:
            print("Restarting")

            start_fishing()

        # Timeout between checking for the fish
        time.sleep(0.1)
