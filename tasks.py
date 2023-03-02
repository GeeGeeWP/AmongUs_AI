import pyautogui
import time

def divert_power():
    for i in [645, 715, 788, 860, 935, 1000, 1075, 1150]:
        pyautogui.moveTo(i, 765)
        pyautogui.drag(0, -83, button='left')
    print("Task Complete")

def accept_power():
    time.sleep(0.5)
    pyautogui.click(900, 585, clicks=1)

def trigger_task(task):
    pyautogui.click(1500, 870, clicks=1)

    if task == "divert_power":
        divert_power()
    elif task == "accept_power":
        accept_power()

