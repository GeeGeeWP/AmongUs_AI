import mss
import mss.tools
import pyautogui
import cv2
from pynput import mouse
from pynput.mouse import Controller
from time import sleep
import math
import navigation
import map_info
import tasks


def grab_screen():
    with mss.mss() as sct:
        sleep(0.3)
        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output='location.png')


def calculate_vector(current_location, target_location):
    neutral_vector = (895, 581)

    vector_x = max(min(neutral_vector[0] + target_location[0] - current_location[0], 1195), 595)
    vector_y = max(min(neutral_vector[1] + target_location[1] - current_location[1], 881), 281)

    hypotenuse = math.sqrt(
        (target_location[0] - current_location[0]) ** 2 + (target_location[1] - current_location[1]) ** 2)
    distance = abs((hypotenuse - 17.1) / 152)
    return vector_x, vector_y, distance


def toggle_map():
    # sleep(0.05)
    pyautogui.click(1560, 314, clicks=2)
    # sleep(0.05)


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
        # toggle_map()

        h, w = template.shape[:2]
        sensitivity = 0.99

        method = cv2.TM_CCORR_NORMED

        res = cv2.matchTemplate(image, template, method)
        res_h, res_w = res.shape[:2]

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

    return [centers[0], navigation.get_a_room(centers[0])]


def move(vector_x, vector_y, distance):
    pyautogui.mouseDown(vector_x, vector_y)
    sleep(distance)
    pyautogui.mouseUp()

    # NOTE: The center is move(895, 581, 3)


if __name__ == '__main__':
    mouse = Controller()
    pyautogui.click(1560, 500, clicks=1)
    region = {'top': 178, 'left': 181, 'width': 1428, 'height': 808}

    location_info = ping_location()
    current_location = location_info[0]
    current_room = location_info[1]
    print("Current Room: " + str(map_info.convert_room_id(current_room)))
    print("Now the location is: " + str(current_location))
    #
    # TODO implement better task system
    task = [[13, 0], [8,0], [14, 0], [5,0], [12, 0], [2, 0], [1, 0]]
    steps = 0
    while (len(task)) > 0:
        print("Length of the task list: " + str(len(task)))

        waypoints, destination_room, kill = navigation.navigate(current_room, task[0])
        print("Current Room: " + str(map_info.convert_room_id(current_room)))
        for i in range(len(waypoints)):
            steps += 1
            print("Steps are: " + str(steps))
            target_location = waypoints[i]
            print("New Target for Waypoint #" + str(i) + " is: " + str(waypoints[i]) + " in " + str(
                map_info.convert_room_id(destination_room)) + " and we are at " + str(
                current_location) + " in " + str(map_info.convert_room_id(current_room)))
            vector_x, vector_y, distance = calculate_vector(current_location, target_location)
            move(vector_x, vector_y, distance)
            current_location = target_location
            current_room = destination_room

            if (steps % 15) == 0 and steps > 0:
                location_info = ping_location()
                current_location = location_info[0]
                current_room = location_info[1]
            # else:
            #     current_location = waypoints[i]
            print("Current Room: " + str(map_info.convert_room_id(current_room)))

        if kill:
            print("Going to Task: " + str(task[0][1]))
            if task[0][1] == 1:
                target_location = tasks.task_locator(task[0])
                vector_x, vector_y, distance = calculate_vector(current_location, target_location)
                move(vector_x, vector_y, distance)
                current_location = target_location
                current_room = destination_room

                tasks.trigger_task(task[0])
            task.pop(0)
            kill = False

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

    # location_info = ping_location()
    # current_location = location_info[0]
    # current_room = location_info[1]
    # navigation.get_a_room(current_location)
    # tasks.stabalize_steering()
    # while True:
    #     print('The current pointer position is {0}'.format(mouse.position))
