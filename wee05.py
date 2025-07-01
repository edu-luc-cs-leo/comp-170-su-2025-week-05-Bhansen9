def intersection(foo:str, bar:str) -> str | None:
    intersection_answer = ""
    if letter in foo:
        if letter in bar and not in intersection_answer:
            intersection_answer += letter
    return intersection_answer if intersection_answer is not "" else None
intersection()

def is_alphabetical(string:str) -> bool:
    counter = 0
    all_alp = True
    while counter < len(string):
        alp_ASCII = ord(string[counter])
        if not(65 <= alp_ASCII <= 90 or 97 <= alp_ASCII <= 122):
            all_alp = False
        counter += 1
    return all_alp

def letter_only(string:str) -> str | None:
    letter_container = ""
    counter_LO = 0
    examinator_LO = ord(string[counter_LO])
    while counter_LO < len(string):
        for char in string:
            if (65 <= examinator_LO <= 90 or 97 <= examinator_LO <=122):
                letter_container += char +
        counter_LO += 1
    return letter_container











#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
