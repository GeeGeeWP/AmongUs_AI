def navigate(current_room, task):
    locations = [(1524, 515),(1021, 407),1,1,1,1,1]

    # origin = locations[current_room]

    # from Upper engine
    if current_room == 3:
        if task == 1:
            waypoint = [(632, 525), (646, 398), (1316, 401)]
        elif task == 2:
            waypoint = [(632, 525), (646, 398), (1014, 399), (1013, 743)]

    elif current_room == 2:
        waypoint = [(1014, 399), (646, 398), (632, 525)]
    return waypoint


def get_a_room(current_location):
    if current_location[0] < 392:
        return 11
    elif current_location[0] < 650:
        if current_location[1] > 1006:
            return 4
        elif current_location[1] < 561:
            return 3
        else:
            print("Hallway!")
    elif current_location[0] < 827:
        if current_location[1] < 887:
            if current_location[1] > 637:
                return 12
            else:
                print("Location Hallway 3")
        else:
            print("Location Hallway 2")
    elif current_location[0] < 1205:
        if current_location[1] < 494:
            print("Location Hallway North")
        elif current_location[1] < 820:
            return 2
        elif current_location[1] < 1293:
            return 5
        else:
            print("Location: Hallway!")
    elif current_location[0] < 1250:
        if current_location[1] > 712:
            return 2
        elif current_location[1] < 1233:
            return 1
    elif current_location[0] < 1640:
        if current_location[1] > 1005:
            if current_location[0] < 1400:
                return 7
            else:
                return 6
        elif current_location[1] < 742:
            return 1
        else:
            print("Location: Hallway connecting Cafeteria - Storage - Admin")
    elif current_location[0] < 1870:
        if current_location[1] < 720:
            return 1
        elif current_location[1] < 1080:
            return 14
        elif current_location[1] > 1320:
            return 7
        else:
            print("Location Hallway connecting Storage - Shields - Communication")
    elif current_location[0] < 1995:
        if current_location[1] > 1310:
            return 7
        elif current_location[1] > 850:
            return 14
        elif current_location[1] < 450:
            print("Location Hallway - Cafeteria - Weapons 3489238")
        else:
            return 13
    elif current_location[0] < 2060:
        if current_location[1] < 450:
            if current_location[0] > 2000:
                return 9
            else:
                print("Location Hallway - Cafeteria - Weapons")
        else:
            return 13
    elif current_location[0] < 2270:
        if current_location[1] < 529:
            return 9
        elif current_location[1] > 1080:
            return 8
        else:
            print("Location Hallway  -  Its a mess")
    elif current_location[0] < 2490:
        print("Location is hallway connecting Nav asdfkjadsokfjspa")
    else:
        return 10
