def scramble(s1, s2):
    letterseen = []
    for letter in s2:
        if not letter in letterseen:
            if s2.count(letter) > s1.count(letter):
                return False
            letterseen += letter
    return True
