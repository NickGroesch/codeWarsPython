def validBraces(string):
    chars = list(string)
    par = 0
    bra = 0
    cur = 0
    top = ""

    def paradd(par):
        par += 1

    def parsub(par):
        par -= 1

    def braadd(bra):
        bra += 1

    def brasub(bra):
        bra -= 1

    def curadd(cur):
        cur += 1

    def cursub(cur):
        cur -= 1

    case = {
        "(": paradd(par),
        ")": parsub(par),
        "[": braadd(bra),
        "]": brasub(bra),
        "{": curadd(cur),
        "}": cursub(cur)
    }

    for char in chars:
        if par < 0 or bra < 0 or cur < 0:
            return False
        case[char]()
        # loc = case[char]
        # fun(loc)
        print(par, bra, cur, top)
        # if
        # top=


validBraces("[({})](]")