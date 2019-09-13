def mutations(a, b, present, turn):
    tried = [present]
    alice = a[:]
    bob = b[:]
    print(len(alice), len(bob))
    for word in alice:  #TODO:this cleaning is not working- very frustrating!
        if len(set(word)) != 4:
            alice.remove(word)
    for word in bob:
        if len(set(word)) != 4:
            bob.remove(word)
    print(len(alice), len(bob))
    print(alice)
    print(bob)
    initial = present
    players = ["alice", "bob"]
    fails = [False, False]
    oneFailed = False
    gameOver = False
    turn = bool(turn)
    player = alice if not turn else bob
    print(present)
    while (not gameOver):
        # print("p", players[turn], player)
        for index, word in enumerate(player):
            if word not in tried:
                if word[:3] == present[:3] or word[1:] == present[1:] or (
                        word[0] == present[0] and word[2:] == present[2:]) or (
                            word[:2] == present[:2] and word[3] == present[3]):
                    present = player[index]
                    tried.append(present)
                    if present in alice:
                        alice.remove(present)
                    if present in bob:
                        bob.remove(present)
                    break
                if index == len(player) - 1:
                    fails[turn] = True
                    if present != initial:
                        return int(not turn)
                    else:
                        oneFailed = True
                if oneFailed and present != initial:
                    return int(not turn)
        if fails[0] == True and fails[1] == True:
            gameOver = True
        print("{0} says {1}".format(players[turn], present))
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

print('xxx', len(set("hill")), set("lilt"))