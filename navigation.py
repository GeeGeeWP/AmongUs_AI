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
    waypoint = []
    current_room = 1
    for i in cafeteria_to_upper_engine:
        waypoint.append(i)
    for i in upper_engine_to_security:
        waypoint.append(i)
    for i in security_to_reactor:
        waypoint.append(i)
    for i in reactor_to_lower_engine:
        waypoint.append(i)
    destination = 7
    # elif current_room == 2:
    #     if task[0] == 3 or 4 or 11 or 12 or 5:
    #         waypoint = [(1018, 510), (986, 402), (625, 404)]
    #         destination = 3
    #     else:
    #         waypoint = [(1018, 510), (1047, 411), (1220, 412)]
    #         destination = 1
    # elif current_room == 3:
    #     waypoint = upper_engine_to_cafeteria
    #     destination = 1
    #     # if task[0] == 1:
    #     #     waypoint = [(632, 525), (646, 398), (1316, 401)]
    #     #     destination = 4
    #     # elif task[0] == 2:
    #     #     waypoint = [(632, 525), (646, 398), (1014, 399), (1013, 743)]
    #     #     destination = 2
    #     # elif task[0] == 12:
    #     #     pass
    #     # elif task[0] == 11:
    #     #     pass
    #     # elif task[0] == 4 or 5 or 6:
    #     #     waypoint = [(631, 517), (541, 529), (537, 1052)]
    #     #     destination = 4
    # elif current_room == 4:
    #     if task[0] == 5:
    #         waypoint = [(636, 1049), (637, 1178), (814, 1188), (847, 1346),(988, 1329), (1018, 1189)]
    #         destination = 5
    #     pass
    # elif current_room == 5:
    #     # if task[0] ==  12 or 11 or 2:
    #     #     waypoint = [(989, 1195), (982, 1342), (855, 1336), (834, 1180), (656, 1175)]
    #     #     destination = 4
    #
    #     if task[0] == 5:
    #         if task[1] == 0:
    #             waypoint = [(1156, 1060), (1000, 920)]
    #             destination = 5
    #             kill = True
    #
    #     else:
    #         waypoint = [(1156, 1060), (1000, 946)]
    #         destination = 5
    # elif current_room == 6:
    #     pass
    # elif current_room == 7:
    #     waypoint = communications_to_shields
    #     destination = 8
    #     # if task[0] == 8 or 13 or 9 or 10:
    #     #     waypoint = [(1896, 1220), (2147, 1189)]
    #     #     destination = 8
    #     # else:
    #     #     waypoint = [(1896, 1220), (1609, 1206)]
    #     #     destination = 6
    # elif current_room == 8:
    #     pass
    # elif current_room == 9:
    #     if task[0] == 13:
    #         waypoint = [(2097, 405), (2152, 473), (2153, 641), (1992, 669)]
    #         destination = 13
    #     elif task[0] == 10:
    #         waypoint = [(2097, 405), (2152, 473), (2153, 641), (2289, 697), (2340, 766), (2564, 757)]
    #         destination = 10
    #     elif task[0] == 8 or 7:
    #         waypoint = [(2097, 405), (2152, 473), (2153, 641), (2291, 848), (2175, 884), (2154, 1183)]
    #         destination = 8
    #     else:
    #         waypoint = [(1774, 414)]
    #         destination = 1
    # elif current_room == 10:
    #     print("2340823709j")
    #     print(task[0])
    #     if task[0] == 13:
    #         print("23487987239876")
    #         waypoint = [(2335, 748), (2267, 673), (1992, 669)]
    #         destination = 13
    #     elif task[0] == 9 or 1 or 2 or 3:
    #         print("8273497826978765")
    #         print(task[0])
    #         waypoint = [(2335, 748), (2289, 697), (2153, 641), (2152, 473), (2097, 405)]
    #         destination = 9
    #     else:
    #         print("Moving")
    #         waypoint = [(2310, 761), (2276, 851), (2158, 883), (2153, 1172)]
    #         destination = 8
    # elif current_room == 11:
    #     pass
    # elif current_room == 12:
    #     pass
    # elif current_room == 13:
    #     # Done
    #     if task[0] == 10:
    #         waypoint = [(2274, 687), (2332, 757), (2561, 767)]
    #         destination = 10
    #     elif task[0] == 8 or 7 or 6:
    #         waypoint = [(2275, 678), (2307, 858), (2160, 872), (2153, 1172)]
    #         destination = 8
    #     elif task[0] == 13:
    #         kill = True
    #     else:
    #         waypoint = [(2156, 665), (2144, 427)]
    #         destination = 9
    # elif current_room == 14:
    #     # Done
    #     if task[0] == 1 or 13 or 9 or 2 or 3 or 10:
    #         waypoint =[(1536, 898), (1517, 522)]
    #         destination = 1
    #     else:
    #         waypoint = [(1536, 898), (1532, 1085)]
    #         destination = 6

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
