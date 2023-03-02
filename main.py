import mss
import mss.tools
import pyautogui
import cv2
import numpy as np
from pynput.mouse import Button, Controller
from time import sleep
import math


def grab_screen():
    with mss.mss() as sct:
        sleep(0.3)
        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output='location.png')

def get_a_room(current_location):
    if current_location[0] < 392:
        print("Location: Reactor!")
    elif current_location[0] < 650:
        if current_location[1] > 1006:
            print("Location Lower Engines")
        elif current_location[1] < 561:
            print("Location Upper Engines")
            return 3
        else:
            print("Hallway!")
    elif current_location[0] < 827:
        if current_location[1] < 887:
            if current_location[1] > 637:
                print("Location Security")
            else:
                print("Location Hallway 3")
        else:
            print("Location Hallway 2")
    elif current_location[0] < 1205:
        if current_location[1] < 494:
            print("Location Hallway North")
        elif current_location[1] < 820:
            print("Location: MedBay!")
            return 2
        elif current_location[1] < 1293:
            print("Location: ELectrical!")
        else:
            print("Location: Hallway!")
    else:
        return

def get_waypoints(current_location):
    pass

def calculate_vector(current_location, target_location):
    neutral_vector = (895, 581)
    # vector_x = neutral_vector[0] + target_location[0] - current_location[0]
    # vector_y = neutral_vector[1] + target_location[1] - current_location[1]

    print(neutral_vector[0])
    print(target_location[0])
    print(current_location[0])
    print(type(neutral_vector[0]))
    print(type(target_location[0]))
    print(type(current_location[0]))
    vector_x = max(min(neutral_vector[0] + target_location[0] - current_location[0], 1195),595)
    vector_y = max(min(neutral_vector[1] + target_location[1] - current_location[1],881),281)

    hypotenuse = math.sqrt(
        (target_location[0] - current_location[0]) ** 2 + (target_location[1] - current_location[1]) ** 2)
    distance = (hypotenuse - 17.1) / 152
    return vector_x, vector_y, distance


def toggle_map():
    # sleep(0.05)
    pyautogui.click(1560, 314, clicks=2)
    #sleep(0.05)

def navigate(current_room, task):
    locations = [(1524, 515),(1021, 407),1,1,1,1,1]

    # origin = locations[current_room]

    # Upper Engine to Medbay
    waypoint = [(632, 525), (1014, 399), (1013, 743)]
    return waypoint



def ping_location():
    toggle_map()
    grab_screen()
    image = cv2.imread('location.png', cv2.IMREAD_COLOR)
    template = cv2.imread('icon.png', cv2.IMREAD_COLOR)
    toggle_map()

    h, w = template.shape[:2]
    sensitivity = 0.99

    method = cv2.TM_CCORR_NORMED

    res = cv2.matchTemplate(image, template, method)
    res_h, res_w = res.shape[:2]

    # fake out max_val for first run through loop
    max_val = 1
    centers = []
    while len(centers) == 0:
        while max_val > sensitivity:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > sensitivity:
                centers.append((max_loc[0] + w // 2, max_loc[1] + h // 2))

                x1 = max(max_loc[0] - w // 2, 0)
                y1 = max(max_loc[1] - h // 2, 0)

                x2 = min(max_loc[0] + w // 2, res_w)
                y2 = min(max_loc[1] + h // 2, res_h)

                res[y1:y2, x1:x2] = 0

                image = cv2.rectangle(image, (max_loc[0], max_loc[1]), (max_loc[0] + w + 1, max_loc[1] + h + 1),
                                      (0, 255, 0))

                cv2.imwrite('output.png', image)
        sensitivity = sensitivity - 0.05
        if sensitivity < 0.5:
            return

    if len(centers) > 2:
        print("Location Fail")
        image = cv2.imread('location.png', cv2.IMREAD_COLOR)
        template = cv2.imread('icon_background.png', cv2.IMREAD_COLOR)
        toggle_map()

        h, w = template.shape[:2]
        sensitivity = 0.99

        method = cv2.TM_CCORR_NORMED

        res = cv2.matchTemplate(image, template, method)
        res_h, res_w = res.shape[:2]

        # fake out max_val for first run through loop
        max_val = 1
        centers = []
        while len(centers) == 0:
            while max_val > sensitivity:
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                if max_val > sensitivity:
                    centers.append((max_loc[0] + w // 2, max_loc[1] + h // 2))

                    x1 = max(max_loc[0] - w // 2, 0)
                    y1 = max(max_loc[1] - h // 2, 0)

                    x2 = min(max_loc[0] + w // 2, res_w)
                    y2 = min(max_loc[1] + h // 2, res_h)

                    res[y1:y2, x1:x2] = 0

                    image = cv2.rectangle(image, (max_loc[0], max_loc[1]), (max_loc[0] + w + 1, max_loc[1] + h + 1),
                                          (0, 255, 0))

                    cv2.imwrite('output.png', image)
            sensitivity = sensitivity - 0.05
            if sensitivity < 0.5:
                return

    print("Current Location is: "+ str(centers[0]))
    print("Current Room is: " + str(get_a_room(centers[0])))
    return [centers[0], get_a_room(centers[0])]


def move(vector_x, vector_y, distance):
    pyautogui.mouseDown(vector_x, vector_y)
    sleep(distance)
    pyautogui.mouseUp()

    # NOTE: The center is move(895, 581, 3)


if __name__ == '__main__':
    mouse = Controller()
    pyautogui.click(1560, 500, clicks=1)
    region = {'top': 178, 'left': 181, 'width': 1428, 'height': 808}

    # sleep(5)
    location_info  = ping_location()
    print("Location Info is: " + str(location_info))
    current_location = location_info[0]
    print("Now the location is: " + str(current_location))
    current_room = location_info[1]
    task = 1
    # # waypoints = [(1528, 502), (1846, 404), (2183, 428), (2158, 684), (2301, 682), (2301, 865), (2138, 870), (2141, 1179), (1612, 1210), (1563, 1050), (1298, 1152), (1283, 1350), (835, 1350), (835, 1172), (652, 1172), (611, 1052), (540, 1056), (537, 548), (630, 496), (653, 407), (1361, 402)]
    waypoints = navigate(current_room, task)
    for i in range(len(waypoints)):
        target_location = waypoints[i]
        print("Am I the error three? " + str(type(target_location)) + " " + str(i))
        print("New Target for Waypoint #" + str(i) + " is: " + str(waypoints[i]) + " and we are at " + str(current_location))
        vector_x, vector_y, distance = calculate_vector(current_location, target_location)
        move(vector_x, vector_y, distance)
        if (i % 9) == 0:
            try:
                location_info  = ping_location()
                current_location = location_info[0]
                current_room = location_info[1]
            except:
                current_location = waypoints[i]
                print("Am I the error too? " + str(type(current_location)))
        else:
            current_location = waypoints[i]
            print("Am I the error? "+ str(type(current_location)))
    #
    #     while abs(current_location[0] - target_location[0]) > 50:
    #         location_info  = ping_location()
    #         current_location = location_info[0]
    #         current_room = location_info[1]
    #         vector_x, vector_y, distance = calculate_vector(current_location, target_location)
    #         move(vector_x, vector_y, distance)
    #         print("Attempted rerouting: " + str(current_location) + " | " + str(target_location))
    #     while abs(current_location[1] - target_location[1]) > 50:
    #         location_info  = ping_location()
    #         current_location = location_info[0]
    #         current_room = location_info[1]
    #         vector_x, vector_y, distance = calculate_vector(current_location, target_location)
    #         move(vector_x, vector_y, distance)
    #         print("Attempted rerouting: " + str(current_location) + " | " + str(target_location))
    # move(600, 581, 2.4)
    # move(1000, 581, 3.7)

    # Move Up and Down
    # move(895, 800, 1.9)
    # move(896, 200, 3)

    location_info = ping_location()
    current_location = location_info[0]
    current_room = location_info[1]
    get_a_room(current_location)
    # while True:
    #     print('The current pointer position is {0}'.format(
    #         mouse.position))