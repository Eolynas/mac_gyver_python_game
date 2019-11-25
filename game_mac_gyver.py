import level as lvl
import MacGyver
import ObjectsPickUp

# Initialisation lvl
level_1 = lvl.Level("config/level_1.txt")

#Initit object
# list_objects = ["aiguille", "tube", "ether"]

object_1 = ObjectsPickUp.ObjectsPickUp(level_1.structure, "aiguille")
object_1.generate_object()
level_1.place_object(object_1)

object_2 = ObjectsPickUp.ObjectsPickUp(level_1.structure, "tube")
object_2.generate_object()
level_1.place_object(object_2)

object_3 = ObjectsPickUp.ObjectsPickUp(level_1.structure, "ether")
object_3.generate_object()
level_1.place_object(object_3)
# level_1.structure[position_x_object_1][position_y_object_1] = name_object_1
# print(level_1.structure)
#initit mac gyver
mac_gyver = MacGyver.MacGyver(level_1.structure)

# Boucle infinie

while True:
    cmd = input('Utiliser ZQSD pour déplacer Mac_Gyver')

    if cmd == "z":
        #On fait monter MG
        mac_gyver.move("up")

    if cmd == "q":
        #On fait aller à droite MG
        mac_gyver.move("left")

    if cmd == "d":
        #On fait aller à gauche MG
        mac_gyver.move("right")

    if cmd == "s":
        #On fait descendre MG
        mac_gyver.move("down")

    if cmd == "o":
        mac_gyver.move("objects")
    if cmd == "e":
        print("PARTIE TERMINEE")
        break

# #initit mac gyver
# mac_gyver = MacGyver.MacGyver(level_1.structure)
# mac_gyver.move("right")
# mac_gyver.move("right")
# mac_gyver.move("down")
# mac_gyver.move("right")