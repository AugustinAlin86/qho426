battery_found = False
while (battery_found == False):
    print("Where should I look?")
    ans1 = input()
    if ans1 == "in the bedroom":
        print("Where in the bedroom should I look?")
        ans2 = input()
        if ans2 == "under the bed":
            print("Found some shoes but no battery")
        else:
            print("Found some mess but no battery")
    elif ans1 == "in the bathroom":
        print("Where in the bathroom should I look?")
        ans2 = input()
        if ans2 == "in the bathtub":
            print("Found rubber duck but no battery")
        else:
            print("Found wet surface but no battery")
    elif ans1 == "in the lab":
        print("Where in the lab should I look?")
        ans2 = input()
        if ans2 == "on the table":
            print("Yes! I found my battery")
            battery_found = True
        else:
            print("Found some tools but no battery")
    else:
        print("I do not know where that is but I will keep looking")