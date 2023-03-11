import pyautogui
import time


def task_locator(task):
    if task[0] == 13:
        if task[1] == 1:
            return (1901, 671)
    if task[0] == 10:
        print("In Nav")
        if task[1] == 1:
            return (1901, 671)


def divert_power():
    time.sleep(0.5)
    for i in [645, 715, 788, 860, 935, 1000, 1075, 1150]:
        pyautogui.moveTo(i, 765)
        pyautogui.drag(0, -83, button='left')
    print("Task Complete")


def accept_power():
    time.sleep(0.5)
    pyautogui.click(900, 585, clicks=1)


def empty_trash():
    print("Empty Trash")
    time.sleep(0.5)
    pyautogui.mouseDown(1170, 492)
    pyautogui.moveTo(1170, 686, 1)
    time.sleep(2)
    pyautogui.mouseUp(0, 0)
    print("Task Complete")


def trigger_task(task):
    pyautogui.click(1500, 870, clicks=1)

    if task[0] == 0:
        divert_power()
    elif task[0] == 13:
        if task[1] == 1:
            empty_trash()
    elif task == "accept_power":
        accept_power()
