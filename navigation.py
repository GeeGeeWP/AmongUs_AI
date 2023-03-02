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
    elif current_location[0] < 1250:
        if current_location[1] > 712:
            print("Location: Medbay!")
        elif current_location[1] < 1233:
            print("Location: Cafeteria! - 437823")
    elif current_location[0] < 1640:
        if current_location[1] > 1005:
            if current_location[0] < 1400:
                print("Location Communications sdjkfna")
            else:
                print("Location: Storage")
        elif current_location[1] < 742:
            print("Location: Cafeteria - 1234")
        else:
            print("Location: Hallway connecting Cafeteria - Storage - Admin")
    elif current_location[0] < 1870:
        if current_location[1] < 720:
            print("Location: Cafeteria - 327867")
        elif current_location[1] < 1080:
            print("Location: Admin - 332877")
        elif current_location[1] > 1320:
            print("Location Communications - 23986374")
        else:
            print("Location Hallway connecting Storage - Shields - Communication")
    elif current_location[0] < 1995:
        if current_location[1] > 1310:
            print("Location Communications - 23423245")
        elif current_location[1] > 850:
            print("Location Admin - 787843")
        elif current_location[1] < 450:
            print("Location Hallway - Cafeteria - Weapons 3489238")
        else:
            print("O2")
    elif current_location[0] < 2060:
        if current_location[1] < 450:
            if current_location[0] > 2000:
                print("Location Weapons - ajifjawnp")
            else:
                print("Location Hallway - Cafeteria - Weapons")
        else:
            print("Location O2")
    elif current_location[0] < 2270:
        if current_location[1] < 529:
            print("Location Weapons - dsfjh")
        elif current_location[1] > 1080:
            print("Location Shields - uaeglbiuwb")
        else:
            print("Location Hallway  -  Its a mess")
    elif current_location[0] < 2490:
        print("Location is hallway connecting Nav asdfkjadsokfjspa")
    else:
        print("Location Navigation")
        return
