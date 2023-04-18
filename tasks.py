import pyautogui
import time


def task_locator(task):
    if task[0] == 13:
        if task[1] == 1:
            return (1901, 671)
    if task[0] == 14:
        if task[1] == 1:
            return (1664, 870)
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


def stabalize_steering():
    time.sleep(0.5)
    pyautogui.click(896, 581)


def connect_wires():
    Wire_R_1 = (1138, 388)
    Wire_R_2 = (1138, 525)
    Wire_R_3 = (1138, 660)
    Wire_R_4 = (1138, 800)
    print("Connecting Wires")
    Wire_L_1 = (625, 388)
    Wire_L_2 = (625, 525)
    Wire_L_3 = (625, 660)
    Wire_L_4 = (625, 800)

    pyautogui.mouseDown(Wire_L_1)
    pyautogui.moveTo(Wire_R_4[0], Wire_R_4[1], 1)
    pyautogui.mouseUp(Wire_R_4[0], Wire_R_4[1])
    time.sleep(0.25)

    pyautogui.mouseDown(Wire_L_2)
    pyautogui.moveTo(Wire_R_1[0], Wire_R_1[1], 1)
    pyautogui.mouseUp(Wire_R_1[0], Wire_R_1[1])
    time.sleep(0.25)

    pyautogui.mouseDown(Wire_L_3)
    pyautogui.moveTo(Wire_R_3[0], Wire_R_3[1], 1)
    pyautogui.mouseUp(Wire_R_3[0], Wire_R_3[1])
    time.sleep(0.25)

    pyautogui.mouseDown(Wire_L_4)
    pyautogui.moveTo(Wire_R_2[0], Wire_R_2[1], 1)
    pyautogui.mouseUp(Wire_R_2[0], Wire_R_2[1])

    print("Task Complete")


def trigger_task(task):
    pyautogui.click(1500, 870, clicks=1)

    if task[0] == 0:
        divert_power()
    elif task[0] == 13:
        if task[1] == 1:
            empty_trash()
    elif task[0] == 14:
        if task[1] == 1:
            connect_wires()
    elif task == "accept_power":
        accept_power()
