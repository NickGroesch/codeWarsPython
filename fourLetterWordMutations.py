def mutations(a, b, present, turn):
    alice = a[:]
    bob = b[:]
    #TODO:need to clean initial lists
    initial = present
    players = ["alice", "bob"]
    fails = [False, False]
    oneFailed = False
    gameOver = False
    turn = bool(turn)
    player = alice if not turn else bob
    # print(present)
    while (not gameOver):
        # print("p", players[turn], player)
        for index, word in enumerate(player):
            if word[:3] == present[:3]:
                present = player[index]
                player.remove(present)
                break
            elif word[1:] == present[1:]:
                present = player[index]
                player.remove(present)
                break
            elif word[0] == present[0] and word[2:] == present[2:]:
                present = player[index]
                player.remove(present)
                break
            elif word[:2] == present[:2] and word[3] == present[3]:
                present = player[index]
                player.remove(present)
                break
            #above checks successful plays, below
            if index == len(player) - 1:
                fails[turn] = not fails[turn]
                # print("fails", fails)
                # print('player {0} fails initial word was {1}, present is {2}'.
                #       format(players[turn], initial, present))
                if present != initial:
                    return int(not turn)
                else:
                    oneFailed = True
            if fails[0] == True and fails[1] == True:
                gameOver = True
        # print("{0} says {1}".format(players[turn], present))
        if oneFailed and present != initial:
            return int(turn)
        turn = not turn
        player = alice if not turn else bob

    return -1


alice = [
    "plat", "rend", "bear", "soar", "mare", "pare", "flap", "neat", "clan",
    "pore"
]
bob = [
    "boar", "clap", "farm", "lend", "near", "peat", "pure", "more", "plan",
    "soap"
]

print(
    # mutations(alice, bob, "maze", 0)  #  0  Alice goes  first, Alice   wins √
    # mutations(alice, bob, "send", 0)  #  1  Alice goes  first, Bob     wins√
    # mutations(alice, bob, "boat", 0)  #  1  Alice fails first, Bob     wins√
    mutations(alice, bob, "apse", 0)  # -1  Alice fails first, neither wins√
    # mutations(alice, bob, "neat", 1)  #  1  Bob   goes  first, Bob     wins
    # mutations(alice, bob, "soar", 1)  #  0  Bob   goes  first, Alice   wins
    # mutations(alice, bob, "mark", 1)  #  0  Bob   fails first, Alice   wins
    # mutations(alice, bob, "calm", 1)  # -1  Bob   fails first, neither wins
)