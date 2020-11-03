def warn_the_sheep(queue):
    counter = len(queue)
    stringOutput = ""
    for i in range(len(queue)):
        if queue[i] == "wolf":
            if counter - 1 == 0:
                stringOutput = "Pls go away and stop eating my sheep"
            else:
                stringOutput = (
                    "Oi! Sheep number "
                    + str(counter - 1)
                    + "! You are about to be eaten by a wolf!"
                )
        else:
            counter -= 1
    print(stringOutput)


warn_the_sheep(["sheep", "sheep", "wolf"])

