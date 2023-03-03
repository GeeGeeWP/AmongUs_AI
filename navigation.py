def navigate(current_room, task):
    kill = False
    if current_room == 1:
        pass
    elif current_room == 2:
        if task[0] == 3 or 4 or 11 or 12 or 5:
            waypoint = [(1018, 510), (986, 402), (625, 404)]
            destination = 3
        else:
            waypoint = [(1018, 510), (1047, 411), (1220, 412)]
            destination = 1
    elif current_room == 3:
        if task[0] == 1:
            waypoint = [(632, 525), (646, 398), (1316, 401)]
            destination = 4
        elif task[0] == 2:
            waypoint = [(632, 525), (646, 398), (1014, 399), (1013, 743)]
            destination = 2
        elif task[0] == 12:
            pass
        elif task[0] == 11:
            pass
        elif task[0] == 4 or 5 or 6:
            waypoint = [(631, 517), (541, 529), (537, 1052)]
            destination = 4
    elif current_room == 4:
        if task[0] == 5:
            waypoint = [(636, 1049), (637, 1178), (814, 1188), (847, 1346),(988, 1329), (1018, 1189)]
            destination = 5
        pass
    elif current_room == 5:
        # if task[0] ==  12 or 11 or 2:
        #     waypoint = [(989, 1195), (982, 1342), (855, 1336), (834, 1180), (656, 1175)]
        #     destination = 4

        if task[0] == 5:
            if task[1] == 0:
                waypoint = [(1156, 1060), (1000, 920)]
                destination = 5
                kill = True

        else:
            waypoint = [(1156, 1060), (1000, 946)]
            destination = 5
    elif current_room == 6:
        pass
    elif current_room == 7:
        pass
    elif current_room == 8:
        pass
    elif current_room == 9:
        pass
    elif current_room == 10:
        pass
    elif current_room == 11:
        pass
    elif current_room == 12:
        pass
    elif current_room == 13:
        pass
    elif current_room == 14:
        pass
    elif current_room == 15:
        pass
    elif current_room == 16:
        pass
    elif current_room == 17:
        pass
    elif current_room == 18:
        pass
    elif current_room == 19:
        pass
    elif current_room == 20:
        pass
    elif current_room == 21:
        pass

    return waypoint, destination, kill


def get_a_room(current_location):
    if current_location[0] < 392:
        return 11
    elif current_location[0] < 650:
        if current_location[1] > 1006:
            return 4
        elif current_location[1] < 561:
            return 3
        else:
            return 15
    elif current_location[0] < 827:
        if current_location[1] < 887:
            if current_location[1] > 637:
                return 12
            else:
                return 16
        else:
            return 21
    elif current_location[0] < 1205:
        if current_location[1] < 494:
            return 16
        elif current_location[1] < 820:
            return 2
        elif current_location[1] < 1293:
            if current_location[0] < 860:
                return 21
            else:
                return 5
        else:
            return 21
    elif current_location[0] < 1250:
        if current_location[1] > 712:
            return 2
        elif current_location[1] < 1233:
            return 1
    elif current_location[0] < 1640:
        if current_location[1] > 1005:
            if current_location[0] < 1400:
                return 6
            else:
                return 6
        elif current_location[1] < 742:
            return 1
        else:
            return 20
    elif current_location[0] < 1870:
        if current_location[1] < 720:
            return 1
        elif current_location[1] < 1080:
            return 14
        elif current_location[1] > 1320:
            return 7
        else:
            return 19
    elif current_location[0] < 1995:
        if current_location[1] > 1310:
            return 7
        elif current_location[1] > 850:
            return 14
        elif current_location[1] < 450:
            return 17
        else:
            return 13
    elif current_location[0] < 2060:
        if current_location[1] < 450:
            if current_location[0] > 2000:
                return 9
            else:
                return 17
        else:
            return 13
    elif current_location[0] < 2270:
        if current_location[1] < 529:
            return 9
        elif current_location[1] > 1080:
            return 8
        else:
            return 18
    elif current_location[0] < 2490:
        return 18
    else:
        return 10
