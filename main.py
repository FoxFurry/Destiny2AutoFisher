import screen_ocr
import pyautogui
import time


def start_fishing():
    pyautogui.keyDown('E')
    time.sleep(2)
    pyautogui.keyUp('E')


if __name__ == '__main__':
    x, y = pyautogui.size()

    # Those are coordinates of the interaction box containing fishing related messages
    # This script reads messages from the box using OCR
    box_x1 = int(x * 0.436)
    box_x2 = int(x * 0.572)
    box_y1 = int(y * 0.659)
    box_y2 = int(y * 0.701)

    ocr_reader = screen_ocr.Reader.create_quality_reader()
    while True:
        results = ocr_reader.read_screen(bounding_box=(box_x1, box_y1, box_x2, box_y2)).as_string()

        if "Go" in results and "Fishing" in results:
            print("Pond detected. Launching loop")

            time.sleep(2)

            break

        print("Waiting for you to approach the fishing pond!")

        time.sleep(1)

    start_fishing()

    # Start fishing loop
    while True:
        results = ocr_reader.read_screen(bounding_box=(box_x1, box_y1, box_x2, box_y2)).as_string()

        if "Catch" in results:
            print("Fish Caught!")
            pyautogui.keyDown('E')
            time.sleep(0.1)
            pyautogui.keyUp('E')

            # Wait for the animation
            time.sleep(3)

            # And restart fishing
            start_fishing()

        # Timeout between checking for the fish
        time.sleep(0.1)
