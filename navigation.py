admin = (1741, 914)
cafeteria = (1524, 525)
communications = (1854, 1425)
electrical = (1020, 1199)
lower_engine = (645, 1183)
medbay = (1032, 740)
navigation = (2603, 750)
o2 = (1998, 673)
reactor = (349, 798)
security = (711, 802)
shields = (2142, 1172)
storage = (1500, 1099)
upper_engine = (645, 539)
weapons = (2169, 414)

admin_to_cafeteria = [(1540, 906), cafeteria]
admin_to_storage = [(1540, 906), storage]
cafeteria_to_admin = [(1540, 906), admin]
cafeteria_to_medbay = [(1335, 399), (1020, 410), medbay]
cafeteria_to_storage = [(1538, 1021), storage]
cafeteria_to_upper_engine = [(1335, 399), (640, 405), upper_engine]
cafeteria_to_weapons = [(1776, 405), (1964, 396), weapons]
communications_to_shields = [(1884, 1234), shields]
communications_to_storage = [(1889, 1213), (1884, 1234), storage]
electrical_to_lower_engine = [(999, 1350), (830, 1356), (833, 1178), (635, 1180), lower_engine]
electrical_to_storage = [(999, 1350), (1341, 1350), (1280, 1167), (1517, 1088), storage]
lower_engine_to_electrical = [(635, 1180), (833, 1178), (830, 1356), (999, 1350), electrical]
lower_engine_to_reactor = [(625, 1045), (550, 1059), (553, 810), reactor]
lower_engine_to_security = [(625, 1045), (550, 1059), (553, 810), security]
lower_engine_to_storage = [(635, 1180), (833, 1178), (830, 1356), (1287, 1352), (1302, 1133), storage]
lower_engine_to_upper_engine = [(625, 1045), (550, 1059), (534, 539), (635, 501), upper_engine]
medbay_to_cafeteria = [(1009, 396), (1344, 408), cafeteria]
medbay_to_upper_engine = [(1009, 396), (622, 398), upper_engine]
navigation_to_o2 = [(2318, 748), (2248, 668), o2]
navigation_to_shields = [(2318, 748), (2276, 851), (2169, 884), shields]
navigation_to_weapons = [(2318, 748), (2248, 668), (2154, 669), (2148, 437), weapons]
o2_to_navigation = [(2311, 672), (2300, 762), navigation]
o2_to_shields = [(2311, 672), (2293, 857), (2156, 859), shields]
o2_to_weapons = [(2143, 671), weapons]
reactor_to_lower_engine = [(553, 810), (628, 1048), lower_engine]
reactor_to_security = [security]
reactor_to_upper_engine = [(553, 810), (536, 515), (636, 532), upper_engine]
security_to_lower_engine = [(553, 810), (628, 1048), lower_engine]
security_to_reactor = [reactor]
security_to_upper_engine = [(553, 810), (536, 515), (636, 532), upper_engine]
shields_to_communications = [(1884, 1234), communications]
shields_to_navigation = [(2157, 887), (2299, 846), (2303, 759), navigation]
shields_to_o2 = [(2157, 887), (2299, 846), (2289, 684), o2]
shields_to_storage = [(2022, 1208), (1605, 1212), (1573, 1104), storage]
shields_to_weapons = [(2157, 887), (2299, 846), (2289, 684), (2162, 678), (2149, 425), weapons]
storage_to_admin = [(1529, 907), admin]
storage_to_cafeteria = [(1538, 1021), cafeteria]
storage_to_communications = [(1590, 1133), (1604, 1218), (1864, 1224), communications]
storage_to_electrical = [(1408, 1097), (1300, 1164), (1293, 1357), (995, 1350), electrical]
storage_to_lower_engines = [(1408, 1097), (1300, 1164), (1293, 1357), (860, 1354), (803, 1174), lower_engine]
storage_to_shields = [(1590, 1133), (1604, 1218), shields]
upper_engine_to_cafeteria = [(1315, 407), cafeteria]
upper_engine_to_lower_engine = [(539, 523), (538, 1083), (628, 1048), lower_engine]
upper_engine_to_medbay = [(647, 400), (1014, 399), medbay]
upper_engine_to_reactor = [(539, 523), (543, 803), reactor]
upper_engine_to_security = [(539, 523), (543, 803), security]
weapons_to_cafeteria = [(1776, 405), cafeteria]
weapons_to_navigation = [(2143, 671), (2300, 762), navigation]
weapons_to_o2 = [(2160, 667), o2]
weapons_to_shields = [(2149, 425), (2162, 678), (2289, 684), (2299, 846), (2157, 887), shields]


def navigate(current_room, task):
    kill = False
    if current_room == admin:
        if task[0] == admin:
            print("Figure out the tasks")
            kill = True
            pass
        elif task[0] == storage or shields or electrical or lower_engine:
            waypoint = admin_to_storage
            destination = storage
        else:
            waypoint = admin_to_cafeteria
            destination = cafeteria
    elif current_room == cafeteria:
        if task[0] == cafeteria:
            print("Figure out the tasks")
            kill = True
            pass
        elif task[0] == weapons or o2 or navigation or shields:
            waypoint = cafeteria_to_weapons
            destination = weapons
        elif task[0] == storage or shields or electrical or lower_engine:
            waypoint = cafeteria_to_storage
            destination = storage
        elif task[0] == admin:
            waypoint = cafeteria_to_admin
            destination = admin
        elif task[0] == medbay:
            waypoint = cafeteria_to_medbay
            destination = medbay
        else:
            waypoint = cafeteria_to_upper_engine
            destination = upper_engine
    elif current_room == communications:
        if task[0] == communications:
            print("Figure out the tasks")
            kill = True
            pass
        elif task[0] == shields or navigation or o2:
            waypoint = communications_to_shields
            destination = shields
        else:
            waypoint = communications_to_storage
            destination = storage
    elif current_room == electrical:
        if task[0] == electrical:
            pass
        elif task[0] == lower_engine or reactor or security or upper_engine or medbay:
            waypoint = electrical_to_lower_engine
            destination = lower_engine
        else:
            waypoint = electrical_to_storage
            destination = storage
    elif current_room == lower_engine:
        if task[0] == current_room:
            pass
        elif task[0] == upper_engine or medbay:
            waypoint = lower_engine_to_upper_engine
            destination = upper_engine
        elif task[0] == security:
            waypoint = lower_engine_to_security
            destination = security
        elif task[0] == reactor:
            waypoint = lower_engine_to_reactor
            destination = reactor
        elif task[0] == electrical:
            waypoint = lower_engine_to_electrical
            destination = electrical
        else:
            waypoint = lower_engine_to_storage
            destination = storage
    elif current_room == medbay:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == upper_engine or security or reactor or lower_engine or electrical:
            waypoint = medbay_to_upper_engine
            destination = upper_engine
        else:
            waypoint = medbay_to_cafeteria
            destination = cafeteria
    elif current_room == navigation:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == o2:
            waypoint = navigation_to_o2
            destination = o2
        elif task[0] == admin or shields or storage or communications or electrical or lower_engine:
            waypoint = navigation_to_shields
            destination = shields
        else:
            waypoint = navigation_to_weapons
            destination = weapons
    elif current_room == o2:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == navigation:
            waypoint = o2_to_navigation
            destination = navigation
        elif task[0] == shields or communications or storage:
            waypoint = o2_to_shields
            destination = shields
        else:
            waypoint = o2_to_weapons
            destination = weapons
    elif current_room == reactor:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == security:
            waypoint = reactor_to_security
            destination = security
        elif task[0] == lower_engine or electrical or storage or communications or admin:
            waypoint = reactor_to_lower_engine
            destination = lower_engine
        else:
            waypoint = reactor_to_upper_engine
            destination = upper_engine
    elif current_room == security:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == reactor:
            waypoint = security_to_reactor
            destination = reactor
        elif task[0] == lower_engine or electrical or storage or communications or admin:
            waypoint = security_to_lower_engine
            destination = lower_engine
        else:
            waypoint = security_to_upper_engine
            destination = upper_engine
    elif task[0] == shields:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == navigation:
            waypoint = shields_to_navigation
            destination = navigation
        elif task[0] == o2:
            waypoint = shields_to_o2
            destination = o2
        elif task[0] == communications:
            waypoint = shields_to_communications
            destination = communications
        elif task[0] == weapons or communications:
            waypoint = shields_to_weapons
            destination = weapons
        else:
            waypoint = shields_to_storage
            destination = storage
    elif current_room == storage:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == admin:
            waypoint = storage_to_admin
            destination = admin
        elif task[0] == communications:
            waypoint = storage_to_communications
            destination = communications
        elif task[0] == electrical:
            waypoint = storage_to_electrical
            destination = electrical
        elif task[0] == shields or navigation or o2:
            waypoint = storage_to_shields
            destination = shields
        elif task[0] == cafeteria or medbay:
            waypoint = storage_to_cafeteria
            destination = cafeteria
        else:
            waypoint = storage_to_lower_engines
            destination = lower_engine
    elif current_room == upper_engine:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == reactor:
            waypoint = upper_engine_to_reactor
            destination = reactor
        elif task[0] == security:
            waypoint = upper_engine_to_security
            destination = security
        elif task[0] == medbay:
            waypoint = upper_engine_to_medbay
            destination = medbay
        elif task[0] == lower_engine or electrical:
            waypoint = upper_engine_to_lower_engine
            destination = lower_engine
        else:
            waypoint = upper_engine_to_cafeteria
            destination = cafeteria
    elif current_room == weapons:
        if task[0] == current_room:
            kill = True
            pass
        elif task[0] == o2:
            waypoint = weapons_to_o2
            destination = o2
        elif task[0] == navigation:
            waypoint = weapons_to_navigation
            destination = navigation
        elif task[0] == shields:
            waypoint = weapons_to_shields
            destination = shields
        else:
            waypoint = weapons_to_cafeteria
            destination = cafeteria

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
